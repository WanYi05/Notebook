# Sets & Tuples!

"""
Sets are similar to lists but are unordered and cannot contain duplications
Use curly brackets
"""

my_set = {1, 2, 3, 4, 5, 1, 2}
print(my_set)
print(len(my_set))

# Sets 不會記憶這些數字的索引值，所以不能 print(my_list[0])

for x in my_set:
    print(x)
    
my_set.discard(3)
print(my_set)

# 從集合中刪除所有值
# my_set.clear() 
# print(my_set)

my_set.add(6)
print(my_set)

my_set.update([7,8])
print(my_set)


# ------------------------------------------

# Tuple

my_tuple = (1, 2, 3, 4, 5)
print(my_tuple)
print(len(my_tuple))
print(my_tuple[1])

# my_tuple[1] = 100 出現錯誤，因tuplr不能指定賦值

# 想要從列表中刪除重複值 -> sets
# 不想要在列表中改變數值時 -> tuple (因不可改變)
# 結論: 最常用 -> list

