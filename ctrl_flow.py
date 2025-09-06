## Control Flow method 

# name = input("Enter your name : ")

# if(len(name) > 5):
#   print("Approved")
# else: 
#   print("Not approved")  


# value = int(input("Enter a value : "))

# if(value < 4):
#   print("Good")
# elif(value == 4):
#   print("OK")  
# else:
#   print("Bad")  

value = 45

match value:
  case _ if(value > 45):
    print("Good")
  case _ if(value == 45):
    print("Equal")
  case _ if(value < 45):
    print("Bad")
  case _ :
    print("BC")