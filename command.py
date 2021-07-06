import os
import pandas as pd
os.system('ls')
df = pd.read_csv("input.csv")
print(df)
for i in range (len(df)):
    print(df.iloc[i,0])
    command = 'youtube-dl -o\"%(upload_date)s.E' + str(i) + '.%(ext)s\"' + ' ' + df.iloc[i,0]
    os.system(command)