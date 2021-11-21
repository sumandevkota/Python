#
# Example file for working with conditional statements
#


def main():
    x = input("Enter the value of X:")
    y = input("Enter the value of Y:")

    # conditional flow uses if, elif, else
    if (x < y):
        print("X is less than Y:")
    elif (x > y):
        print("X is greater than Y:")
    else:
        print("X is equal to Y:")            

    # conditional statements let you use "a if C else b"
    st = "X is less than Y" if(x<y) else "x is greater than or the same as y"
    print(st)
     

if __name__ == "__main__":
    main()
  
