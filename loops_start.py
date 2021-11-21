#
# Example file for working with loops
#

def main():
  x = 0

  # define a while loop
 # while (x<5):
  # x = x + 1




  # define a for loop
#for r in range (5, 10):
 #  print(r)

  # use a for loop over a collection
#shop = ["milk","egg","beer","onions","tomatoes","bread"]
#for q in shop:
#    print(q)


  
  # use the break and continue statements
#for x in range (5, 10):
  #if( x== 8): break
 # if ( x % 2 == 0): continue #skipped even numbers
  #print(x)


  #using the enumerate() function to get index 
shop = ["milk","egg","beer","onions","tomatoes","bread"]
for i,d in enumerate(shop):
  print(i, d)




if __name__ == "__main__":
  main()
