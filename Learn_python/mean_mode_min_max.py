
l = input ("Please Entre a size of a list ") # taking the length of a list from user
l = int(l)
my_list = [ ]                                # defining an empty list

for i in range(l) :                          # running for loop until the length of list to get the input from the user as a list elements
 y = input ("Entre number ")                 #tsaking input one at a time
 my_list.append(y)                           #adding all enteed number to a list

print("Your list has been successfully created") #printing the list just to display 
for i in range (0,len(my_list)): #using for loop to convert string to integer
 my_list[i] = int(my_list[i])    #converting every elements in list to integer



print(my_list)                                  #display the list
mean = sum(my_list)/len(my_list)                #calculating mean 
print ("the maximun numbers is ",max(my_list))  #calculating and displaying maximun number in the list 
print ("the minimun numbers is ",min(my_list))  #calculating minimun number in the list 
print ("the mean of the numbers is  ", mean)    #displaying mean








