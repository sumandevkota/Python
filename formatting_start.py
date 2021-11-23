#
# Example file for formatting time and date output
#

from datetime import datetime

def main():
  # Times and dates can be formatted using a set of predefined string
  # control codes 
  #days= ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
  now = datetime.now()
  print(now)

  #### Date Formatting ####
 
  # %y/%Y - Year, %a/%A - weekday, %b/%B - month, %d - day of month
  print(now.strftime("The current year is :%y"))  # using uppercase placeholder gives full
  print(now.strftime("The current month is :%B")) # using lowercase place holder gives shortform
  print(now.strftime("The current day is :%d"))
  print(now.strftime("The current Weekday is :%a"))
  #print("Which is :",days[])
  

  # %c - locale's date and time, %x - locale's date, %X - locale's time
  print(now.strftime("local Date and time : %c"))
  print(now.strftime("local Date: %x"))
  print(now.strftime("local time : %X"))
  #### Time Formatting ####
  
  # %I/%H - 12/24 Hour, %M - minute, %S - second, %p - locale's AM/PM
  print(now.strftime("Current time : %I:%M:%S %p"))
  print(now.strftime("24-Hour time : %H:%M"))
if __name__ == "__main__":
  main();
