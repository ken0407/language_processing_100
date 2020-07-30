word_1 = 'paraparaparadise'
word_2 = 'paragraph'

word_1_letter_list = [s_ for letter in word_1]
word_2_letter_list = [s_ for letter in word_2]

word_1_letter_bi_gram = []
word_2_letter_bi_gram = []
for idx in range(len(word_1_letter_list) - 1):
    word_1_letter_bi_gram.append(''.join([word_1_letter_list[idx], word_1_letter_list[idx+1]]))

for i in range(len(word_2_letter_list) - 1):
    word_2_letter_bi_gram.append(''.join([word_2_letter_list[i], word_2_letter_list[i+1]]))

X = set(word_1_letter_bi_gram)
Y = set(word_2_letter_bi_gram)

print(f'union: {X.union(Y)}')
print(f'intersection: {X.intersection(Y)}')
print(f'difference: {X.difference(Y)}')

if 'se' in X:
    print('se is in X.')
else:
    print('se is not in X.')

if 'se' in Y:
    print('se is in Y.')
else:
    print('se is not in Y.')