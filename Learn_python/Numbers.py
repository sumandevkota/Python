# this program performs a arithmetic operation of two number by converting the given input to a interger 
# when a user gives an input python takes it as a string 


a = input("Enter a first number ") #taking input from user here I am asking number but python takes it as a string
b = input("Entre a Second Number ")#taking input from user here I am asking number but python takes it as a string
x = float(a)  # changing the input string to integer 
y = float(b)  # changing the input string to integer

c = x + y # Addition of two integer

d = x - y # Subtracting two integer 
e = x * y # multiplying Two integer 
f = x / y # dividing two integer the result here is float 

print("The addition of two number is : ", c)        #displaying result as a form of output
print("The difference of two number is : ", d)      #displaying result as a form of output  
print("The Multiplication  of two number is : ", e) #displaying result as a form of output
print("The division  of two number is : ", f)       #displaying result as a form of output
