import pandas as pd
from matplotlib import pyplot as plt

data = pd.read_csv("data.csv")
df = pd.DataFrame(data)

male = 0
female = 0
for i in df.index:
    if (df.loc[i,'Sex'] == 0):
        male= male + 1
       
    else:
        female = female + 1
       
    
print("\t\t\t\n Number of males: ",male)
print("\t\t\t\n Number of females: ",female)

df['Sex'] = df['Sex'].values.astype(str)

df['Sex'] = df['Sex'].str.replace('0','M')
df['Sex'] = df['Sex'].str.replace('1','F')

print(df['Sex'])

plt.hist(df['Sex'])
plt.xlabel("Male and Female")
plt.ylabel("Count")
plt.grid(color = 'g',linestyle = '--',linewidth = 0.5)
plt.show()







