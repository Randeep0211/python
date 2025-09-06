#### Variables #### 

# In python if a variable is declared again with a value it considers the latest one for the print. 
value_one = "Randeep"
value_one = "Singh"
print(value_one)


# In python a variable can't be undeclared or without a value. 
# If no value to be assigned then simply declare None as a good practice. 
value_two = None
print(value_two)

# In python there are multiple specific keywords pre-defined as specific features or methods. 
# This keywords should strictly not be used as variable names as good practices. 
# This keywords even if declared as variables would be valid as there is no lock on them like JS. 

# print = 3 # Not to be used like this

name = input("Enter your name : ")
# print(name)

value = input("Enter a value : ")
# print(value)

# How to substitute variables in a string statement.Just make sure to put 'f' before string in print()

value_three = "Randeep"
age = 30
print(f"The name is {value_three} and age is {age}")

