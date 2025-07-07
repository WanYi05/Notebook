# Loops!

"""
For & While Loops
"""

my_list = [1, 2, 3, 4, 5]

# print(my_list[0])
# print(my_list[1])
# print(my_list[2])
# print(my_list[3])
# print(my_list[4])

# for iterator in my_list:
#     print (iterator)

# for x in my_list:
#     print(x)

# for x in range(3, 6):
#     print(x)

sum_of_for_loop = 0

for x in my_list:
    sum_of_for_loop += x
    
print(sum_of_for_loop)

# ---------------------------------

my_list = ["Monday", "Tuesday", "Wednesday", "Thrusday"]

for x in my_list:
    print(f"Happy {x}!")

# ----------------------------

i = 0

# while i < 5:
#     i += 1
#     print(i)

while i < 5:
    i += 1
    if i == 3:
        continue
    print(i)
    if i == 4:
        break
else:
    print("i is now larger or equal to 5")

# ----------------------------

# Assignment

"""
Given: my_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

 - Create a while loop that prints all elements of the [my_list] variable 3 timess
 
 - When printing the elements, use a [for loop] to print the elements
 
 - However, if the element of the [for loop is equal to Monday], continue without printing
 
"""

my_list = ["Moday", "Tuesday", "Wednesday", "Thursday", "Friday"]

x = 0
while x < 3:
    x += 1
    for i in my_list:
        if i == "Monday":
            print("-----------")
            continue
        print(i)

