import timeit
print("Performing Arithmetic Operation to determine execution time\n")
print("A = 3\tB = 7\n")
# addition
print("Addition\n") 
start = timeit.default_timer()
A = 3
B = 7
C = A + B
print("Addition of 3 & 7: ",C)
stop = timeit.default_timer()
execution_time = stop - start
print("Time to add: ", execution_time)
print("\n")
# Subtraction
print("Substraction\n")
start = timeit.default_timer()
C = A - B
stop = timeit.default_timer()
execution_time = stop - start
print("Substraction of 3 & 7:",C)
print("Time to subtract: ", execution_time)
print("\n")
# Multiplication 
print("Multiplication\n")
start = timeit.default_timer()
C = A * B
stop = timeit.default_timer()
execution_time = stop - start
print("Multiplication of 3 & 7:",C)
print("Time to Multiply: ", execution_time)
print("\n")
# Division
print("Division\n")
start = timeit.default_timer()
C = A / B
stop = timeit.default_timer()
execution_time = stop - start
print("Division of 3 & 7",C)
print("Time to Divide:", execution_time)


