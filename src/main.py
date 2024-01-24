import pandas as pd

RATIO = 0.05

df = pd.read_csv('./data/daily_TECL_filtered.csv') 

df['signal'] = 0

for i in range(len(df)):
    p = df.iloc[i]['open']
    
    for j in range(i+1, len(df)):
        if df.iloc[j]['close'] > p * (1 + RATIO):
            df.at[i,'signal'] = round(100 / (j - i))
            break
        elif df.iloc[j]['close'] < p * (1 - RATIO):
            df.at[i,'signal'] = -round(100 / (j - i))
            break
            
df.to_csv('./data/daily_TECL_signals.csv', index=False)

print("done!")