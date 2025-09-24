import pandas as pd
import pickle
import os
from tqdm import tqdm
# Sample data mimicking your structure
files = os.listdir('/home/soumya/pipeline/LLM-Playground/YaraGen/Data/Synthetic_250k')
df = pd.DataFrame()

for file in files:
    if file.endswith('.pkl'):
        print(f'Loading {file}...')
        data = pickle.load(open(f'/home/soumya/pipeline/LLM-Playground/YaraGen/Data/Synthetic_250k/{file}', 'rb'))
        df = pd.concat([df, pd.DataFrame(data)], ignore_index=True)

print(df.head())
print(f'Total records: {len(df)}')
# File path for your training data
text_file_path = 'synthetic250k_placeholder.txt'

# --- Extract text and save to file ---
with open(text_file_path, 'w', encoding='utf-8') as f:
    for index, row in df.iterrows():
        # Write both the English and YARA text to the file
        # Each piece of text gets its own line
        f.write(row['translation_placeholder']['en'] + '\n')
        f.write(row['translation_placeholder']['yara'] + '\n')

print(f"Data successfully written to {text_file_path}")