# If Else!

"""
Flow Control: If Else Elif
"""

x = 2

if x > 1:
    print("x is greater than 1")

else: 
    print("x is not greater than 1")


print("Outside of if statement")

# ------------------------------------

hour = 21

if hour < 15:
    print("Good morning!")
elif hour < 20:
    print("Good afternoon!")
else:
    print("Good night!")

# ------------------------------------

"""
Assignment!

 - Create a variable [grade] holding an integer between [0-100]
 
 - Code [if, elif, else statements] to print the letter grade of the number grade variable
 
 Grades:
 
 A = 90 - 100
 
 B = 80 - 89
 
 C = 70 - 79
 
 D = 60 - 69
 
 F = 0 - 59
 
"""
grade = int(input())
 
if grade >= 90:
     print("A")
     
elif 80 <= grade < 90:
    print("B")

elif 70 <= grade < 80:
    print("C")
    
elif 60 <= grade < 70:
    print("D")

else:
    print("F")
