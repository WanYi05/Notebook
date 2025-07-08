"""
Dictionaries
"""

user_dictionary = {
    'username': 'codingwithroby',
    'name': 'Eric',
    'age': 32
}

# print(user_dictionary)

print(user_dictionary.get('username'))
print (len(user_dictionary))

user_dictionary["married"] = True
user_dictionary.pop("age")
user_dictionary.clear()

del user_dictionary # del刪除(user_dictionary)後就無法print出來了，會造成錯誤

# --------------------------

for x in user_dictionary:
    print(x)
    
for x, y in user_dictionary.items():
    print(x, y) 

# --------------------------

user_dictionary2 = user_dictionary.copy()
user_dictionary2.pop('age')
print(user_dictionary2) 

# --------------------------
# Dictionaries Assignment

"""
Based on the dictionary:

my_vehicle = {
    'model': 'Ford',
    'make': 'Explorer',
    'year': 2018,
    'mileage': 40000
}
 
 - Create a [for loop] to print all keys and values
 - Create a new variable [vehicle2], which is a copy of [my_vehicle]
 - Add a new key [number_of_tires] to the [vehicle2] variable that is equal to 4
 - [Delete] the mikeage key and value from [vehicle2]
 - [Print] just the keys from [vehicle2]
"""

my_vehicle = {
    'model': 'Ford',
    'make': 'Explorer',
    'year': 2018,
    'mileage': 40000
}

for x, y in my_vehicle.items():
    print(x, y)

vehicle2 = my_vehicle.copy()
vehicle2["number_of_tires"] = 4
vehicle2.pop("mileage")
print(vehicle2)

for i in vehicle2:
    print(i)
