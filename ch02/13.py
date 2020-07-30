import subprocess

import pandas as pd

NUM_COLUMNS = 2
FILENAME_TEMPLATE = '../data/col{}.txt'

for i in range(NUM_COLUMNS):
    df = pd.concat([
        pd.read_csv(FILENAME_TEMPLATE.format(i), sep='\t', header=None) for i in range(NUM_COLUMNS)
    ], axis=1)
    print(df.head())
    subprocess.run(
        f"paste {' '.join([FILENAME_TEMPLATE.format(i) for i in range(NUM_COLUMNS)])}| head -n 5", shell=True
    )
