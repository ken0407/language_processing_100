import click
import pandas as pd
import subprocess

FILEPATH = '../data/popular-name.txt'


@click.command()
@click.option('-n', help='num of rows to print', type=int, required=True)
def print_tails(n: int) -> None:
    """自然数Nをコマンドライン引数などの手段で受け取り，入力のうち末尾のN行だけを表示

    :param n:表示したい行数
    """
    click.echo(pd.read_csv(FILEPATH, sep='\t', header=None).tail(n))


if __name__ == '__main__':
    subprocess.run(f"tail -n 5 {FILEPATH}", shell=True)
    print_tails()

