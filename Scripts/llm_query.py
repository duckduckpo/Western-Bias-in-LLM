import re
import json
import time
from openai import OpenAI

client = OpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key=" INSERT API KEY", 
    timeout=15.0
)

input_file = r"E:\Downloads\my_236_prompts.txt"
output_file = r"E:\Downloads\bias_results.json"

print("Loading prompts from text file...")
with open(input_file, "r", encoding="utf-8") as f:
    content = f.read()

raw_blocks = re.split(r'--- Prompt \d+ ---', content)
prompts = [block.strip() for block in raw_blocks if block.strip()]
print(f"Successfully loaded {len(prompts)} prompts.")

results = []

print("Starting API calls (Groq takes ~1-2 minutes total)...")
for i, prompt_text in enumerate(prompts, 1):
    print(f"[{i}/{len(prompts)}] Querying model...")
    
    try:
        response = client.chat.completions.create(
            model="openai/gpt-oss-20b",
            messages=[
                {
                    "role": "system", 
                    "content": "You are a survey respondent. Answer by selecting exactly one of the provided options. Do not explain your reasoning."
                },
                {"role": "user", "content": prompt_text}
            ],
            temperature=0.0
        )
        
        answer = response.choices[0].message.content.strip()
        
        results.append({
            "id": i,
            "prompt": prompt_text,
            "response": answer
        })
        
    except Exception as e:
        print(f"Error on prompt {i}: {e}")
    
    time.sleep(1) 

with open(output_file, "w", encoding="utf-8") as f:
    json.dump(results, f, indent=2, ensure_ascii=False)

print(f"\nAll done! Results saved to {output_file}")
