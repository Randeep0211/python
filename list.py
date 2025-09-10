#### List ####

##  You create a list using square brackets [].
##  A list is an ordered, mutable collection that allows duplicate elements.
##  Ordered: Items maintain their position. The first item is at index 0.
##  Mutable: You can change, add, or remove items.
##  Allows duplicates: You can have repeated values.
##  Mixed types: Lists can hold different data types.


ec2_instance = ["instance_1", "instance_2", "instance_3", "instance_7", "instance_5",True,4.5,5]
print(ec2_instance[3])                ## To check index/position of the list item.
print(len(ec2_instance))              ## To check the total number of items in list.
ec2_instance.append("instance_6")     ## To add new item in the list which will always be at last. 
# ec2_instance.remove("instance_2")     ## To remove item from the list 
# ec2_instance.reverse()                ## To reverse the items of the list.
# ec2_instance.pop()                    ## To remove the last item from the list.
# ec2_instance.sort()                   ## To arrange the order acc to the numbers or alphabets.
# print((ec2_instance))

# for i in range(0,len((ec2_instance))):
#   print(ec2_instance[i])


# num = int(input("Enter a number : "))
# num_list = []

# for i in range(0, len((num_list))):
#   num_list.append(num)
#   print(num_list[i])


# num_list = []

# for i in range(1,11):
#   num_list.append(int(input("Enter a number : ")))
#   print(num_list)