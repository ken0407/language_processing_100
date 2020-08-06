from gensim.models import KeyedVectors
import numpy as np

model = KeyedVectors.load_word2vec_format('../data/GoogleNews-vectors-negative300.bin.gz', binary=True)

def cos_similarity(x,y):
    return np.dot(x, y) / (np.linalg.norm(x) * np.linalg.norm(y))

print(cos_similarity(model['United_States'], model['U.S.']))