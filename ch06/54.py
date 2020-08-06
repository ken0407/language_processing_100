from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score
import pandas as pd
import numpy as np

train = pd.read_csv('train.feature.txt', sep='\t')

use_cols = list(filter(lambda x: x.islower(), train.columns))

le = LabelEncoder()
train['PUBLISHER_LABEL'] = le.fit_transform(train['PUBLISHER'])

model = LogisticRegression(max_iter=1000)
model.fit(train[use_cols], train['PUBLISHER_LABEL'])

def predict(model, X):
    return [model.predict(X), np.max(model.predict_proba(X), axis=1)]

test = pd.read_csv('test.feature.txt', sep='\t')

print(accuracy_score(le.transform(test['PUBLISHER']), model.predict(test[use_cols])))
