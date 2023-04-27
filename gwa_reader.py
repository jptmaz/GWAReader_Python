# Write a Python program that read a file containing the name of 20 students together with their GWA. 
# The program will output the name of the student who got the highest GWA (including the GWA).

# Open and read the text file containing the names of students and their GWA.

import sys

with open("C:/Users/HomePC/OOP_SourceCode/GWAReader/class_list.txt") as file_reader:
    student_file = file_reader.readlines()
    highest_student_name = ""
    highest_student_gwa = ""
    # Enter the highest grade a student may get
    highest_gwa = 1.00
    # Separate the student's name from their GPA.
    for line in student_file:
        student_name, student_gwa = line.split(", ")
        student_gwa = float(student_gwa)
        #print(student_name)
        #print(student_gwa)
                
        # Check each GPA and compare it to the highest grade attainable.
        if highest_gwa < student_gwa < 1.75:
            print(student_gwa)
            

    
# Print the name of the student with the highest grade and their GPA.
#print (highest_student)   
    
