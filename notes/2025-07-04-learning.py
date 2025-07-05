# 2025-07-04 學習筆記

"""
String Formatting
"""


first_name = "Wan"

sentence = "Hi {}"
last_name = "Lin"
print(sentence.format(first_name, last_name))

print(f"Hi {first_name} {last_name} I hope you are learning")
# --------------------------------------------------------------
"""
User Input
"""

first_name = input("Enter your first name: ")
days = input("How many days before your birthday: ")
print(f"Hi {first_name}, only {days} "
        f"before your birthday!") 
# ------------------------------------------------------
"""
String Assignment we will do together:

Ask the user how many days until their birthday

Week is = 7 days

decimals within the return is allowed...
"""

days = int(input("How many days until your birthday? "))

print(round(days/7, 2))
# ------------------------------------------------------
"""
Lists are a collection of data
"""

my_list = [80, 96, 72, 100, 8]
print(my_list[4])

people_list = ["Ken", "Justin", "William"]
print(people_list[-1])

