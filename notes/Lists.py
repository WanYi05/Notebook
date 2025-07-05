"""
Lists are a collection of data
"""

my_list = [80, 96, 72, 100, 8]
print(my_list[1])
print(my_list[0:4])

my_list.append(1000)
print(my_list)

my_list.insert(2, 500) #在第二的索引處放入500
print(my_list)

my_list.remove(72) #將數字72從列表中刪除
print(my_list)

my_list.pop(0) #將索引值0(數字80)從列表中刪除
print(my_list)

my_list.sort()
print(my_list)

# -------------

people_list = ["Ken", "Justin", "William"]
print(people_list[-1])
print(len(people_list))
print(people_list[0:2])

"""
List Assignment
  - Creat a "list" of 5 animals called "zoo"
  - Delete the animal at the "3rd index".
  - "Append" a new animal at the end of the list
  - "Delete" the animal at the beginning of the list.
  - "Print" all the animals
  - "Print" only the first 3 animals
"""

zoo = ['Monkey', 'Zebra', 'Gorilla', 'Lion', 'Tiger']

zoo.pop(3)
zoo.append('Lizard')
zoo.pop(0)
zoo.insert(0, 'Lizard')
print(zoo)

for x in zoo:
    print(x)

print(zoo[0:3])


