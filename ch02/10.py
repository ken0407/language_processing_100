import subprocess

import pandas as pd

FILEPATH = '../data/popular-name.txt'
df = pd.read_csv(FILEPATH, sep='\t', header=None)

print(f'length: {len(df)}')
subprocess.run(f'wc -l {FILEPATH}', shell=True)
