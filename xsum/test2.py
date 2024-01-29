from datasets import load_dataset

# Load the XSum dataset
dataset = load_dataset('xsum')

# Access the training set
train_dataset = dataset['train']

# Get the size of the training set
size_of_train_dataset = len(train_dataset)

print(f"Size of Training Dataset: {size_of_train_dataset}")

print(train_dataset[0]["document"])

