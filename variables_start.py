# 
# Example file for variables
#

# Declare a variable and initialize it
f = 0
#print(f)




# re-declaring the variable works
#f = "abc"
#print(f)



# ERROR: variables of different types cannot be combined
#print("this is a string" + str(123)) # str() changes integer to string



# Global vs. local variables in functions
def somefunction():
    global f
    f = 'def'
    print(f)

del f #del deletes the variable
print(f)

