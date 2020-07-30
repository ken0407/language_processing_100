text = 'I am an NLPer'

word_bi_gram = []
word_list = text.split(' ')
for i in range(len(word_list) - 1):
    word_bi_gram.append(' '.join([word_list[i], word_list[i+1]]))

letter_bi_gram = []
letter_list = [letter for letter in text]
for i in range(len(letter_list) - 1):
    letter_bi_gram.append(' '.join([letter_list[i], letter_list[i+1]]))

print(f'word_bi_gram: {word_bi_gram}')
print(f'letter_bi_gram: {letter_bi_gram}')
