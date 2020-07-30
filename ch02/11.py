import subprocess

import pandas as pd

FILEPATH = '../data/popular-name.txt'
df = pd.read_csv(FILEPATH, sep='\t', header=None)

print(f'{df.head()}')
subprocess.run(f"cat {FILEPATH} | tr '\t' ' ' | head -n 5", shell=True)
