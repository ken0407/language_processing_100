text = (
    'Hi He Lied Because Boron Could Not Oxidize Fluorine.'
    ' New Nations Might Also Sign Peace Security Clause. Arthur King Can.'
)

element_dict = {}
one_words = [i-1 for i in [1, 5, 6, 7, 8, 9, 15, 16, 19]]
for i, word in enumerate(text.split(' ')):
    if i in one_words:
        w = word[:1]
    else:
        w = word[:2]
    element_dict.update({w: i+1})

print(element_dict)