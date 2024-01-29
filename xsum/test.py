from datasets import load_dataset
from openai import OpenAI
import os
import time

# Function to save the last processed index
def save_last_processed_index(index, filename="last_processed_index.txt"):
    with open(filename, "w") as f:
        f.write(str(index))

# Function to read the last processed index
def read_last_processed_index(filename="last_processed_index.txt"):
    if os.path.exists(filename):
        with open(filename, "r") as f:
            return int(f.read().strip())
    return 0

# Initialize the OpenAI client with your API key
client = OpenAI(api_key='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')

# Load the XSum dataset
dataset = load_dataset('xsum')
train_dataset = dataset['train']

# Directory to save the summaries
directory_path = './summaries'
os.makedirs(directory_path, exist_ok=True)

# Read the last processed index
last_processed_index = read_last_processed_index()

# Set the maximum number of documents to process for the demo
max_documents = 200

attempt  = 0
while 1:
# Iterate over the documents in the training set starting from the last processed index
    for i in range(last_processed_index+1, min(last_processed_index + max_documents +1, len(train_dataset))):
        file_id = train_dataset[i]['id']
        document = train_dataset[i]['document']

        sum_file_path = os.path.join(directory_path, f"{i}-{file_id}.sum")
        print(f"processing {i}-{file_id}")
        print(f"document:{document[0:50]}...")
        # Skip if summary file already exists
        if not os.path.exists(sum_file_path):
            # Use OpenAI API to generate the summary
            try:
                response = client.completions.create(
                    model="gpt-3.5-turbo-instruct",
                    prompt=document+"\n use one sentence to summarize it",
                    max_tokens=200
                )
                response_text = response.choices[0].text
                assert response_text!=""
                print(f"response:{response_text[0:50]}.....")

                # Save the summary to a new file
                with open(sum_file_path, 'w') as sum_file:
                    sum_file.write(response_text)

                # Save the current index
                save_last_processed_index(i)
            except  AssertionError as e:
                break
            except Exception as e:
                print(f"Error at document {i}: {e}")
                time.sleep(20)
                break

print(f"Summarization completed up to document index: {i}")

