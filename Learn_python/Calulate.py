def calc(x,y,op):
 a = float(x)     # converting given interger to a float 
 b = float(y)
 if op == '+' :   #using if else state ment to choose the operation based on input op
     z = a + b
     print("the addition of two given number is ",z)
 elif op == '-':
    z = a - b
    print("the difference of given two number is ",z)

 elif op == '*':
    z = a * b    
    print ("the multiplication of given number is ",z)

 else :
    if b == 0:
        print ('division not possible')
    else:    
       z = a/b 
       print ('the division of the numbers is ',z)       

calc (2,0,'+')
