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

for label, coef in zip(model.classes_, model.coef_):
    print(f'{label}_top10: {np.array(use_cols)[np.argsort(coef)[::-1][:10]]}')
    print(f'{label}_worst10: {np.array(use_cols)[np.argsort(coef)[:10]]}')
