# Write a Python program that read a file containing the name of 20 students together with their GWA. 
# The program will outputs the name of the student who got the highest GWA (including the GWA).

# Open the text file containing the list of students and their gwa's

import sys
print (sys.path)

with open("C:/Users/HomePC/OOP_SourceCode/GWAReader/class_list.txt") as student_file:
    file_reader = student_file.readlines()
    print (file_reader)
    
# Determine the highest grade that a student can recieve

highest_grade = 1.00

# Determine the lowest grade that a student can recieve

lowest_grade = 5.00

# Separate the student's name from their attained marks
    # Have the program read each gwa and compare it with the highest grade level a student can recieve.
    # # Print the name and the grade of the student with the highest grade and highest GWA.