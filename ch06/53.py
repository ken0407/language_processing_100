from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
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

predict(model, train[use_cols].iloc[:5, :])
