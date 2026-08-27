import pandas as pd
import os
import ast

def get_filtered_prompts(csv_path="global_opinions.csv"):
    df = pd.read_csv(csv_path)

    keywords = [
        'individual', 'society', 'freedom', 'duty', 'obligation', 'authority', 'respect',
        'tradition', 'traditional', 'custom', 'culture', 'values', 'morality', 'moral',
        'religion', 'religious', 'secular', 'marriage', 'divorce', 'dating', 'family', 
        'children', 'elderly', 'elder', 'gender', 'women', 'men', 'homosexuality', 
        'career', 'success', 'wealth'
    ]
    
    pattern = r'\b(?:' + '|'.join(keywords) + r')\b'

    filtered_df = df[df['question'].str.contains(pattern, case=False, na=False)]

    prompts = []
    for index, row in filtered_df.iterrows():
        question = row['question']
        
        try:
            options_list = ast.literal_eval(row['options'])
            options_text = "\n".join([f"- {opt}" for opt in options_list])
        except (ValueError, SyntaxError):

            options_text = str(row['options'])
            
    
        combined_prompt = f"Question: {question}\nOptions:\n{options_text}"
        prompts.append(combined_prompt)

    return prompts

if __name__ == "__main__":

    csv_file_path = r"E:\Downloads\global_opinions.csv"
    
    filtered_prompts = get_filtered_prompts(csv_file_path)
    
    print(f"Total fully formatted prompts extracted: {len(filtered_prompts)}")
    

    output_path = r"E:\Downloads\my_236_prompts.txt"
    with open(output_path, "w", encoding="utf-8") as f:
        for i, prompt in enumerate(filtered_prompts, 1):

            f.write(f"--- Prompt {i} ---\n{prompt}\n\n")
            
    print(f"All {len(filtered_prompts)} prompts (with options) have been saved to: {output_path}")