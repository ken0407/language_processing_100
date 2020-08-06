from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

train = pd.read_csv('train.feature.txt', sep='\t')

use_cols = list(filter(lambda x: x.islower(), train.columns))

model = LogisticRegression(max_iter=1000)
model.fit(train[use_cols], train['PUBLISHER'])

def predict(model, X):
    return [model.predict(X), np.max(model.predict_proba(X), axis=1)]

test = pd.read_csv('test.feature.txt', sep='\t')
labels = test['PUBLISHER'].unique()
pred = model.predict(test[use_cols])

train_scores = []
test_scores = []
for i in range(10):
    model = LogisticRegression(max_iter=10000, C=10**(i-5))
    model.fit(train[use_cols], train['PUBLISHER'])
    train_scores.append(accuracy_score(train['PUBLISHER'], model.predict(train[use_cols])))
    test_scores.append(accuracy_score(test['PUBLISHER'], model.predict(test[use_cols])))

plt.plot([i-5 for i in range(10)], train_scores, label='train')
plt.plot([i-5 for i in range(10)], test_scores, label='test')
plt.xlabel('parameter')
plt.ylabel('accuracy')
plt.legend()
plt.savefig('fig.png')
