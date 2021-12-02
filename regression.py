import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt


data = { 
       
       "Area" : [2600,3000,3200,3600,4000],
 
       "Price" : [550000,565000,610000,68000,725000]

       }
#load data into a DataFrame object:
df = pd.DataFrame(data)
print(df)
#creating a scatter plot of Area vs Price
plt.scatter(df['Area'], df['Price'],marker = "*")
#plt.show()
reg = LinearRegression()
X = df['Area'].values.reshape(-1,1)
y = df['Price'].values.reshape(-1,1)

reg.fit(X,y)
w = reg.coef_
b = reg.intercept_
score = reg.score(X,y)

print(f'weight = {w}')
print(f'intercept = {b}')
print(f'score = {score}')

