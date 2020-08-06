from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import optuna
import tempfile

train = pd.read_csv('train.feature.txt', sep='\t')
valid = pd.read_csv('valid.feature.txt', sep='\t')
test = pd.read_csv('test.feature.txt', sep='\t')

use_cols = list(filter(lambda x: x.islower(), train.columns))

def optimization_func(trial):
    l1_ratio = trial.suggest_uniform('l1_ratio', 0, 1)
    C = trial.suggest_loguniform('C', 1e-4, 1e4)
    model = LogisticRegression(max_iter=10000, l1_ratio=l1_ratio, C=C)
    model.fit(train[use_cols], train['PUBLISHER'])

    return accuracy_score(valid['PUBLISHER'], model.predict(valid[use_cols]))

study = optuna.create_study(direction='maximize')
study.optimize(optimization_func, timeout=3600)

trial = study.best_trial
model = LogisticRegression(max_iter=10000, l1_ratio=trial.params['l1_ratio'], C=trial.params['C'])
print(accuracy_score(test['PUBLISHER'], model.predict(test[use_cols])))