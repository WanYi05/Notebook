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

print("-------------")

people_list = ["Ken", "Justin", "William"]
print(people_list[-1])
print(len(people_list))
print(people_list[0:2])
