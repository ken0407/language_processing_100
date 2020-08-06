from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
import pandas as pd

train = pd.read_csv('train.feature.txt', sep='\t')

use_cols = list(filter(lambda x: x.islower(), train.columns))

le = LabelEncoder()
train['PUBLISHER_LABEL'] = le.fit_transform(train['PUBLISHER'])

model = LogisticRegression(max_iter=1000)
model.fit(train[use_cols], train['PUBLISHER_LABEL'])
