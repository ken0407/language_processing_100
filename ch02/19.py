import subprocess

import pandas as pd

FILENAME = '../data/popular-name.txt'
df = pd.read_csv(FILENAME, sep='\t', header=None)

print(df.iloc[:, 0].value_counts())
subprocess.run(f"cut -f 1 {FILENAME} | sort | uniq | head -n 5", shell=True)

# ToDo
