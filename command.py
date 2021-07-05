import os
import pandas as pd
os.system('ls')
df = pd.read_csv("input.csv")

for i in range (len(df)):
    print(i)
    command = 'youtube-dl' + ' ' + df.iloc[i,0]
    os.system(command)
