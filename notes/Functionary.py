"""
Functions
"""

# print("Hello and welcome to functions!")

def my_fuction():
    print("Inside my_fuction")
    
my_fuction()
# ---------------------
def print_my_name(name):
    print(f"Hello {name}!")

print_my_name("Wan")
# ---------------------
def print_my_name(first_name, last_name):
    print(f"Hello {first_name} {last_name}!")

print_my_name("Wan", "Lin")
# ---------------------
# ---------------------
def print_color_red():
    color = "Red"
    print(color)
       
color =  "Blue"
print(color)    
print_color_red()
# ---------------------
def print_numbers(highest_number, lowest_number):
    print(highest_number)
    print(lowest_number)
        
print_numbers(10, 3)
print_numbers(lowest_number = 3, highest_number = 10)
# ---------------------
def multiply_numbers(a, b):
    return a * b
        
solution = multiply_numbers(10, 6)
print(solution)
# ---------------------
def print_list(list_of_numbers):
    for x in list_of_numbers:
        print(x)
        
number_list = [1,2,3,4,5]
print_list(number_list)
# ---------------------
def buy_item(cost_of_item):
    return cost_of_item + add_tax_to_item(cost_of_item)
    
def add_tax_to_item(cost_of_item):
    current_tax_rate = .03
    return cost_of_item * current_tax_rate
    
final_cost = buy_item(50)
print(final_cost)
# ---------------------
# Functions Assignment

"""

 - Create a [function] that takes in [3 parameters (firstname, lastname, age)] and returns a [dictionary] based on those values

"""

def user_dictionary (firstname, lastname, age):
    created_user_dictionary = {
        "firstname": firstname,
        "lastname": lastname,
        "age": age
    }
    return created_user_dictionary
    
solution_dictionary = user_dictionary(firstname = "Wan", lastname = "Lin", age = 30)

print(solution_dictionary)
