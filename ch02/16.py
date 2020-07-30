import click
import pandas as pd
import subprocess

FILEPATH = '../data/popular-name.txt'


@click.command()
@click.option('-n', help='num of rows to print', type=int, required=True)
def print_split(n: int) -> None:
    """自然数Nをコマンドライン引数などの手段で受け取り，入力のファイルを行単位でN分割

    :param n:表示したい行数
    """
    df = pd.read_csv(FILEPATH, sep='\t', header=None)
    length = len(df) // n
    for i in range(n):
        if i == n-1:
            click.echo(df.iloc[length*i: length*(i+1), :].head())
        else:
            click.echo(df.iloc[length * i:, :].head())


if __name__ == '__main__':
    subprocess.run(f"split {FILEPATH} 5 | xargs cat", shell=True)
    print_split()

# ToDo

