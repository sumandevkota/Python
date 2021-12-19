import pandas as pd
import numpy as np
from matplotlib import pyplot as plt 
import seaborn as sns




# Here i am using train.csv to train and then test it with test.csv 

train = pd.read_csv("train.csv") # reading the train.csv file

#understanding the data 
print("\t\t\tThe information on Data\n\n\n")
info_train = train.info()        # putting dataset information into a variable



# Describe() gives the central tendencies of the data 
# in other words it seperates numeric columns from non numeric coulmns
describe_train = train.describe()
print("\t\t\t This is described data \n\n\n")
print(describe_train)
print(describe_train.columns) # printing the all numeric columns

# seperating numeric columns from non numeric
# theses are the data that we want to understand using a histogram
num_train = train[['PassengerId','Survived','Pclass','Age','SibSp','Parch','Fare']]
print("\t\t\t This is numeric column\n\n\n")
print(num_train)



#  creating histogram plot of the given numeric data 
# check if the histrogram follows normal distrubution 
#for i in num_train.columns:
 #   plt.hist(num_train[i])
  #  plt.title(i)
   # plt.show()



# seperating non numeric column and assinging it to a variable 
#we want to understand this with a value count
non_train = train[['Survived','Pclass','Sex','Ticket','Cabin','Embarked']]
#print(non_train)


# understand the different relationship with the data
# using correlation 
print(num_train.corr())
sns.heatmap(num_train.corr())
plt.show()



# to compare the survival rate across age, sibsp, Parch, Fair
SR = pd.pivot_table(train, index = 'Survived', values = ['Age','SibSp','Parch','Fare'])
print(SR)


# bar plot observation of data
for i in non_train.columns:
    sns.barplot(non_train[i].value_counts().index,non_train[i].value_counts()).set_title(i)
    plt.show()


# to check the Survival of each catagorical variable

print(pd.pivot_table(train, index = 'Survived',columns = 'Pclass',values = 'Ticket',aggfunc = 'count'))

print(pd.pivot_table(train, index = 'Survived',columns = 'Sex',values = 'Ticket',aggfunc = 'count'))

print(pd.pivot_table(train, index = 'Survived',columns = 'Embarked',values = 'Ticket',aggfunc = 'count'))



  


    

