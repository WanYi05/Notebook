# Imports

"""
 - Modules get used all the time throughout
    programming
 - It helps with creating more files,
    with unique purposes, to help with 
    clean maintainable code.
"""

homework_assignment_grades = {
    'homework_1': 85, 
    'homework_2': 100,
    'homework_3': 81
}

def calculate_homework(homework_assignments_arg):
    sum_of_grades = 0
    for homework in homework_assignments_arg.values():
        sum_of_grades += homework
    final_grade = sum_of_grades / len(homework_assignments_arg)
    print(final_grade)
    

calculate_homework(homework_assignment_grades)
