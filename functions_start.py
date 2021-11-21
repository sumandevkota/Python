#
# Example file for working with functions
#

# define a basic function
def function_1():
    print("This is a function_1")


# function that takes arguments
def function_2(arg1,arg2):
    print(arg1, " " ,arg2)



# function that returns a value
def cube(x):
    l = x*x*x
    return(l)


# function with default value for an argument
def power (num, x = 2):
    result = 1
    for i in range(x):
        result = result * num
    return result



#function with variable number of arguments
def multi_add(*args): # * means to pass variable number of argument
    answer = 0
    for x in args:
        answer = answer + x
    return answer


#function_1()         # calling function directly
#print(function_1())  # calling function inside print 
#print(function_1)    #function is not being excuted because of  no ()
#function_2(10,20)    # executing function with argument
#print(cube(3))       #executing function with return value
                      
#print(power(2))
print(power(num = 3 , x = 3))
print(power(5))
print(multi_add(1,2,3,4,5,6,7,8,9,10))


