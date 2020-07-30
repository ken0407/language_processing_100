import random


def typoglycemia(text: str) -> str:
    """スペースで区切られた単語列に対して，長さが４文字より長い時各単語の先頭と末尾の文字は残し,
    それ以外の文字の順序をランダムに並び替える関数

    :param text: 文字列
    :return: 入力が4文字より長い時の並び替えた文字列
    """
    if len(text) <= 4:
        return text
    else:
        return text[0] + ''.join(random.shuffle([letter for letter in text[1:-1]])) + text[-1]


sample_text = (
    'I couldn’t believe that I could actually understand'
    ' what I was reading : the phenomenal power of the human mind .'
)
print(typoglycemia(sample_text))
