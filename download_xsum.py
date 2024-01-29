from datasets import load_dataset

dataset = load_dataset("EdinburghNLP/xsum")

import pandas as pd

# Convert the 'train' split to a DataFrame
df_train = pd.DataFrame(dataset['train'])
print(df_train)

