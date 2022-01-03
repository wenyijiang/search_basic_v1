from gensim.models import word2vec

sentences = word2vec.Text8Corpus("/Users/jiangwenyi/code/search_basic/data/nlp/learn_word2vec/uk_ecoms_data/desc.txt")
model = word2vec.Word2Vec(sentences, vector_size=100, hs=1, min_count=1, window=3)

sim = model.wv.most_similar("easter", topn=20)
print(sim)