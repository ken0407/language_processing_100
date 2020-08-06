import string
from typing import Iterable
import re

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

train = pd.read_csv('train.txt', sep='\t')
valid = pd.read_csv('valid.txt', sep='\t')
test = pd.read_csv('test.txt', sep='\t')

def preprocessing_text(text: str) -> str:
    replace_table = str.maketrans(string.punctuation, ' '*len(string.punctuation))
    return re.sub(r'[0-9]+', '0', text.translate(replace_table).lower())

vec_tfidf = TfidfVectorizer(min_df=10, ngram_range=(1,2))
train_vec_feature = vec_tfidf.fit_transform([preprocessing_text(text) for text in train['TITLE']])
tfidf_train = pd.concat([
    train, 
    pd.DataFrame(train_vec_feature.toarray(), columns=vec_tfidf.get_feature_names())
    ], axis=1)

valid_vec_feature = vec_tfidf.transform([preprocessing_text(text) for text in valid['TITLE']])
tfidf_valid = pd.concat([
    valid, 
    pd.DataFrame(valid_vec_feature.toarray(), columns=vec_tfidf.get_feature_names())
    ], axis=1)

test_vec_feature = vec_tfidf.transform([preprocessing_text(text) for text in test['TITLE']])
tfidf_test = pd.concat([
    test, 
    pd.DataFrame(test_vec_feature.toarray(), columns=vec_tfidf.get_feature_names())
    ], axis=1)


tfidf_train.to_csv('train.feature.txt', sep='\t', index=False)
tfidf_valid.to_csv('valid.feature.txt', sep='\t', index=False)
tfidf_test.to_csv('test.feature.txt', sep='\t', index=False)
