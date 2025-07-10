# Imports

"""
 - Modules get used all the time throughout
    programming
 - It helps with creating more files,
    with unique purposes, to help with 
    clean maintainable code.
"""

import Imports.grade_average_service as grade_service

homework_assignment_grades = {
    'homework_1': 85, 
    'homework_2': 100,
    'homework_3': 81
}


grade_service.calculate_homework(
    homework_assignment_grades
)

# VS Code執行時，終端機要輸入: python -m Imports.homework_grades 
# 注意路徑要在 Imports 上一層


