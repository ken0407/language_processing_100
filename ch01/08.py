def cipher(text: str) -> str:
    """与えられた文字列の各文字を英小文字ならば(219 - 文字コード)の文字に置換, その他の文字はそのまま出力する関数

    :param text: 文字列
    :return: 変換した文字列
    """
    return ''.join([chr(219 - ord(letter)) if letter.islower() else letter for letter in text])


sample_text = 'the quick brown fox jumps over the lazy dog'
print(f'変換前: {sample_text}')
print(f"暗号化: {cipher(sample_text)}")
print(f"暗号化: {cipher(cipher(sample_text))}")
