import re

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

with open('../data/neko.txt', mode='r') as f:
  original_neko = f.read()

noun_list = []
for sentense in whole_sentense_list:
    for i, word in enumerate(sentense):
        if word['pos'] == '名詞':
            noun_list.append(word['surface'])
for word in set(noun_list):
    pattern = r'({})+'.format(word)
    ans = set(re.findall(pattern, original_neko))
    if len(ans)>1:
        print(ans)
