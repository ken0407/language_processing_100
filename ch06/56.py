from sklearn.linear_model import LogisticRegression
from sklearn.metrics import precision_score, recall_score, f1_score
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

precision = list(precision_score(test['PUBLISHER'], pred, average=None, labels=labels))
precision.append(precision_score(test['PUBLISHER'], pred, average='micro'))
precision.append(precision_score(test['PUBLISHER'], pred, average='macro'))

recall = list(recall_score(test['PUBLISHER'], pred, average=None, labels=labels))
recall.append(recall_score(test['PUBLISHER'], pred, average='micro'))
recall.append(recall_score(test['PUBLISHER'], pred, average='macro'))

f1 = list(f1_score(test['PUBLISHER'], pred, average=None, labels=labels))
f1.append(f1_score(test['PUBLISHER'], pred, average='micro'))
f1.append(f1_score(test['PUBLISHER'], pred, average='macro'))

df = pd.DataFrame({'precision': precision, 'recall': recall, 'f1': f1}, index=list(labels)+['マイクロ平均', 'マクロ平均'])
print(df)
