import pandas as pd

data = pd.read_csv("/Users/jiangwenyi/code/search_basic/data/nlp/learn_word2vec/uk_ecoms_data/data.csv")

data = data['Description'].to_numpy()
data = list(set(data))
data = [str(x).lower() + "\n" for x in data]
with open("/Users/jiangwenyi/code/search_basic/data/nlp/learn_word2vec/uk_ecoms_data/desc.txt", 'w') as f:
    f.writelines(data)
