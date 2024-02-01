
import pandas as pd

import glob


data_paths = glob.glob('cleaned_one_review.csv')
print(data_paths)

df = pd.DataFrame()

for path in data_paths:
    df_temp = pd.read_csv(path)
    df_temp.columns = ['titles','reviews']

    df_temp.dropna(inplace=True)
    df = pd.concat([df,df_temp],ignore_index=True)


df.drop_duplicates(inplace=True)
df.info()
df.to_csv('./review_cleaned.csv',index=False)
