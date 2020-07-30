from typing import Union


def template(x: int, y: str, z: Union[int, float]) -> str:
    """引数x, y, zを受け取り「x時のyはz」という文字列を返す関数

    :param x: 時刻
    :param y: 種類
    :param z: 値
    :return: レンダリングされたテンプレート
    """
    return f'{x}時の{y}は{z}'


print(template(12, '気温', 22.4))
