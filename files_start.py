#
# Read and write files using the built-in Python file methods
#

def main():  
  # Open a file for writing and create it if it doesn't exist

  #f = open("textfile.txt","w+") # to create file
  #f = open("textfile.txt","a")   # open file in append mode
  f = open("textfile.txt","r")  # open file in read mode


  # Open the file for appending text to the end
  
     
  # write some lines of data to the file
  #for i in range(10):
   # f.write("This is line " + str(i) + "\r\n")
    #f.write("Suman_Devkota\n")

  
  # close the file when done
  #f.close()
  
  # Open the file back up and read the contents
  if f.mode == 'r':
   # contents = f.read() to read all file
   fl = f.readline()
   for x in fl:
    print(x)
  #print(contents)  
    
if __name__ == "__main__":
  main()
