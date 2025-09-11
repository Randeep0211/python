#### Set ####

## A set is an unordered, mutable, and unindexed collection of unique elements. It has {} constructor.
# - No duplicates allowed
# - Unordered: No guarantee of item order
# - Unindexed: You can't access items by position
# - Mutable: You can add or remove items
# - Efficient: Great for fast membership tests (in)

# my_set = {1,3,2,4,3,8,6}
# my_set.add(78)
# my_set.remove(3)
# my_set.discard(6)
# my_set.pop()             ## Here pop removes the initial item unlike in list. 
# my_set.clear()
# print(my_set)

set_one = {1,3,5,7}
set_two = {2,10,3,4,5,7,8}


# print(set_one.union(set_two))
## Output : {1, 2, 3, 4, 5, 7, 8}

# print(set_one.intersection(set_two))
## Output : {3, 5, 7}

# print(set_one.difference(set_two))
## output : {1}

# print(set_one.symmetric_difference(set_two))
# output: {1,2,4,8,10}
