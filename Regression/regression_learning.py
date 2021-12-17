import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

print("\n\n\t\t\tThis is a regression Analysis\n") # Printing Just a title

data = pd.read_csv("Regression.csv") # Reading a data
print(data)
#print(data[:10])  # printing just first 10 rows
x = data['x']    # assining 'x' column to a variable x
y = data['y']    # assining 'y' column to a variable y

plt.scatter(x,y)  # generating scatter plot using plt.scatter from matplotlib.pyplot
plt.xlabel('X')
plt.ylabel('y')
plt.show()        # displaying the scatter plot

# Training and testing data
x_train , x_test , y_train , y_test = train_test_split(x,y)
# Train Test Data visualization
plt.scatter(x_train,y_train, label = "Training Data",color = 'r',alpha = 0.7)
plt.scatter(x_test,y_test, label = "Testing Data",color = 'g',alpha = 0.7)
plt.legend()
plt.title("Trainning And Testing Data")
plt.legend()
plt.show()

#print(data.head(10)) # displays first 10 rows of the datasets

#creating linlear model
reg = LinearRegression()
reg.fit(x_train.values.reshape(-1,1),y_train.values.reshape(-1,1)) # reshape needed to make data 2D


# use model to predict on test data
prediction = reg.predict(x_test.values.reshape(-1,1))
plt.plot(x_test, prediction, label = "Linear Regression", color = 'b')
plt.scatter(x_test,y_test, label ="Actual Test Data", color = 'y', alpha = 0.7 )
plt.legend()
plt.show()

# prediction 
p = reg.predict(np.array([[20]])) [0]
print(p)

# determine the score
s = reg.score(x_test.values.reshape(-1,1),y_test.values.reshape(-1,1))
print("Regression Score: \n",s)

# regression coefficient/ weight
w = reg.coef_
print("Weight: \n",w)

# Regression intercept
b = reg.intercept_
print("Intercept: \n",b) 



 









                      


