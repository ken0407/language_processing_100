import pandas as pd
import sklearn

df = pd.read_csv('../data/newsCorpora.csv', sep='\t', header=None)
df.columns = ['ID', 'TITLE', 'URL', 'PUBLISHER', 'CATEGORY', 'STORY', 'HOSTNAME', 'TIMESTAMP']
df = sklearn.utils.shuffle(df[df['PUBLISHER'].isin(['Reuters', 'Huffington Post', 'Businessweek', 'Contactmusic.com', 'Daily Mail'])])
unit_of_length = len(df) // 10
train = df.iloc[:unit_of_length*8, :]
valid = df.iloc[unit_of_length*8:unit_of_length*9, :]
test = df.iloc[unit_of_length*9:, :]

print(f'all_df_shape: {df.shape}')
print(f'train_shape: {train.shape}')
print(f'valid_shape: {valid.shape}')
print(f'test_shape: {test.shape}')

train.to_csv('train.txt', sep='\t', index=False)
valid.to_csv('valid.txt', sep='\t', index=False)
test.to_csv('test.txt', sep='\t', index=False)
