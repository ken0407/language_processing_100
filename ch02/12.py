import subprocess

import pandas as pd

NUM_COLUMNS = 2
FILEPATH = '../data/popular-name.txt'
df = pd.read_csv(FILEPATH, sep='\t', header=None)

filename_template = '../data/col{}.txt'

for i in range(NUM_COLUMNS):
    df.iloc[:, i].to_csv(filename_template.format(i), index=False, header=False)
    print(filename_template.format(i))
    print(df.iloc[:, i].head())
    subprocess.run(f"cat {filename_template.format(i)} | tr '\t' ',' | cut -f {i+1} -d ',' | head -n 5", shell=True)
