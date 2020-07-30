import subprocess

import pandas as pd

FILENAME = '../data/popular-name.txt'
df = pd.read_csv(FILENAME, sep='\t', header=None)

print(df.sort_values(by=2, ascending=False).head())
subprocess.run(f"cat {FILENAME} | sort -rnk 3 | head -n 5".split(' '), shell=True)

# ToDo