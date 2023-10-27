import pandas as pd

df = pd.read_csv('event.csv') 

for index, row in df.iterrows():
    if not pd.isna(row['checked_in_at']): 
        print(row['name'])
