import re
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder

with open('../data/neko.txt.mecab', mode='r') as f:
    neko = f.read()
neko = neko.replace('\t', ',').replace('\u3000', ',')
neko_list = neko.split('\n')

# 表層形（surface），基本形（base），品詞（pos）
whole_sentense_list = []
sentense_list = []
for word in neko_list:
    if word == 'EOS':
        if len(sentense_list) == 0:
            pass
        else:
            whole_sentense_list.append(sentense_list)
        sentense_list = []
        continue
    word_info = word.split(',')
    if word_info[0] == '':
        continue
    else:
        sentense_list.append({'surface': word_info[0], 'base': word_info[5], 'pos': word_info[1]})
whole_sentense_list = whole_sentense_list[1:]

word_dict = {}
for sentense in whole_sentense_list:
    for word in sentense:
        if word['pos'] != '特殊':
            surface = word['surface']
            if surface in word_dict:
                word_dict[surface]+=1
            else:
                word_dict[surface] = 1

df = pd.DataFrame({'word':list(word_dict.keys()), 'count': list(word_dict.values())})
df.sort_values(by='count', ascending=False, inplace=True)

df['rank'] = df['count'].rank(ascending=False)
plt.scatter(np.log(df['rank']), np.log(df['count']))
plt.xlabel('rank')
plt.ylabel('appear_times')
plt.savefig('zipf.png')
