word_1 = 'パトカー'
word_2 = 'タクシー'

word = ''
for idx in range(len(word_1)):
    word += word_1[idx]
    word += word_2[idx]
print(word)