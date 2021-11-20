#
# Example file for HelloWorld
#
# print("Hello Word!!")            # simple print statement
# name = input("Enter your name:") # taking input as a string
# print("Nice to meet you,",name)  # printing the variable name

def main():
    print("This is my first function defined")
    print("This is a hello_World file")
    age = input("Please enter your age:") # number entered will be string datatype
    age = int(age)
    if(age % 2 == 0):
        print("You entered an even number!!!")
    else:
        print("you entered a odd number!!!") 

if __name__ == "__main__": # helps to execute a function in a program
    main()                 



