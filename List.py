new_list= ['apple', 'orange', 12, ['peanut', 'butter', 'jelly', 'time']]

print(new_list)
print(len(new_list))
print(type(new_list[2]))
num = new_list[2]
obj = new_list[1]

print(f"I have {num} {obj}'s")

print("I have ", new_list[2], new_list[1])

#i like jelly on my toast
# newlist  has 4 elements
# element 3 of new list is a list

jell = new_list[3][2]
print(jell)
print(f"I like {jell} on my toast")

print(new_list[2])
print(new_list[-1])

print(new_list[:3])

for item in new_list[:3]:
  print(item)

new_list[0]= 'banana'
print(new_list)

# 

new_list.append(23)
print(new_list)

list1= []

for i in range(10):
  list1.append(i)

print(list1)

# 

new_list.insert(0, 'grape')

print(new_list)

# 

del new_list[2]
del new_list[-1]
print(new_list)

# 

food= ['burger', 'fries', 'pizza', 'hotdog']
food_item= food.pop()
food_item2= food.pop(1)

print(food_item)
print(food_item2)

# 

transportation= ['planes', 'trains', 'automobiles', 'boats']

transportation.remove('automobiles')
item_remove= 'trains'
transportation.remove(item_remove)

print(transportation)
print(item_remove)

# 

instruments= ['piano', 'flute', 'guitar', 'trumpet']

instruments.sort()

print(instruments)

# 

instruments.sort(reverse=True)

print(instruments)

# 

instruments= ["Piano", 'flute', 'guitar', 'Guitar', 'trumpet']
mixed_list= ['piano', '1', 'trumpet', '5']

example_sorted_function = sorted(instruments)
print(example_sorted_function)
print(instruments)
example_sort_method = instruments.sort()
print(example_sort_method)
print(instruments)

# 

instruments= ['piano', 'flute', 'guitar', 'trumpet']

print(sorted(instruments))

# 

furniture= ['couch', 'chair', 'bed', 'table']

furniture.reverse()

print(furniture)

# 

# # This does NOT copy a list:
furniture2= furniture
print(furniture2)

# # Valerie's Example
original_list = [1, 2, 3]
new_reference = original_list  # new_reference is now another name for the same list object

new_reference.append(4)  # Modifying the list via new_reference

print("Original List:", original_list)  # Output: Original List: [1, 2, 3, 4]
print("New Reference:", new_reference)  # Output: New Reference: [1, 2, 3, 4]
print(original_list == new_reference)

# # # What does this show.....
# # # It shows that line 7 is NOT how we copy an obhect.
# # # line 7 only adds a new reference to the existing object.

# # # how DO we copy a list??


# Valerie's REAL Copy options:
original_list = ["A", "B", "C"]
copied_list = original_list.copy()  # copied_list is now a separate object with the same contents

copied_list.append(4)  # Modifying the copied list does not affect the original list

print("Original List:", original_list)  # Output: Original List: [A, B, C]
print("Copied List:", copied_list)  # Output: Copied List: [A, B, C, 4]
print(original_list == copied_list)
# In this example, original_list remains unchanged even though copied_list
#  is modified. This shows that copied_list is indeed a separate list.

# 

furniture2.append("armoire")

print(furniture2)
print(furniture)

# 

transportation= ['planes', 'trains', 'automobiles', 'boats']

# Option#2  creating a list of the object (its a slice from beginning to end, so it will be identical)
new_transportation= transportation[:]
new_transportation.append('bicycle')

print(new_transportation)
print(transportation)
print(transportation == new_transportation)