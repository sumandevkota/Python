import pandas as pd
import numpy as np 
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from matplotlib import pyplot as plt


train = pd.read_csv("train.csv")


# test train split


X_train, X_test , y_train, y_test = train_test_split (train.x, train.y)
# visualization of train and test data
#plt.scatter(X_train,y_train, label = "Training Data", color = 'g', alpha = 0.7)
#plt.scatter(X_test,y_test, label = "Training Data", color = 'r', alpha = 0.7)
#plt.show()

# create linear model  using train data
LR = LinearRegression()
LR.fit(X_train.values.reshape(-1,1),y_train.values.reshape(-1,1)) 
#reshapping the values to make data 2D

# using test data to predict
Predict = LR.predict(X_test.values.reshape(-1,1))
plt.plot(X_test,Predict, label = "Linear Regression", color = 'b')
plt.scatter ( X_test,y_test, label ="Actual Test Data", color= 'g', alpha = 0.7)
plt.legend()
plt.show()

# prediction using our model 
p100 = LR.predict (np.array([[100]]))[0]
print("IF X = 100, OUR model Prediction Value is: \n")
print(p100)

# regression score
s = LR.score(X_test.values.reshape(-1,1),y_test.values.reshape(-1,1))
print("Score of our model: \n",s)

# regression intercept 
b = LR.intercept_ 
print("Intercept of the model: \n",b)

# regression Coefficient
w = LR.coef_
print("Coefficient of our Model: \n",w)






