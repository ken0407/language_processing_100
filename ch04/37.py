import re
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

count_dict = {}
for sentense in whole_sentense_list:
  sentense = [word['surface'] for word in sentense]
  if '猫' in sentense:
    for word in sentense:
      if word not in count_dict:
        count_dict[word] = 1
      else:
        count_dict[word]+=1

cat_df = pd.DataFrame({'word': list(count_dict.keys()), 'count': list(count_dict.values())})
cat_df = cat_df[cat_df['word']!='猫']
cat_df.sort_values(by='count', ascending=False, inplace=True)
print(cat_df.head(10))
