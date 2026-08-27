import json
import matplotlib.pyplot as plt

# Change this filename to your other JSON file when ready to run the second chart
INPUT_FILE = r'E:\Downloads\bias_resultsqwen.json'

# Load the LLM's generated answers
with open(INPUT_FILE, 'r', encoding='utf-8') as f:
    results = json.load(f)
    
# Load your independent scoring rubric
with open(r'E:\Downloads\scoring_key.json', 'r', encoding='utf-8') as f:
    scoring_key = json.load(f)

counts = {"Western": 0, "Non-Western": 0, "Neutral/Other": 0}

# Helper function to handle both single strings and lists in the scoring key
def matches_expected(answer, expected_value):
    if expected_value is None:
        return False
    if isinstance(expected_value, list):
        return answer in expected_value
    return answer == expected_value

# Compare the LLM's answers against the Answer Key
for item in results:
    q_id = str(item['id'])
    llm_answer = item['response'].strip()
    
    if q_id in scoring_key:
        expected_western = scoring_key[q_id].get('western')
        expected_non_western = scoring_key[q_id].get('non_western')
        
        if matches_expected(llm_answer, expected_western):
            counts["Western"] += 1
        elif matches_expected(llm_answer, expected_non_western):
            counts["Non-Western"] += 1
        else:
            counts["Neutral/Other"] += 1

# Generate the Pie Chart
labels = list(counts.keys())
sizes = list(counts.values())
colors = ['#ff9999','#66b3ff','#99ff99']

plt.figure(figsize=(8, 6))
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
plt.title(f'LLM Cultural Bias Distribution ({INPUT_FILE})')
plt.axis('equal') 
plt.show()