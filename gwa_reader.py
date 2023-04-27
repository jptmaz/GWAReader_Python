# Write a Python program that read a file containing the name of 20 students together with their GWA. 
# The program will outputs the name of the student who got the highest GWA (including the GWA).

# Open the text file containing the list of students and their gwa's

with open("C:/Users/HomePC/OOP_SourceCode/GWAReader/class_list.txt") as student_file:
    file_reader = student_file.readlines()
    class_record_dict = {}
       
    # Separate the student's name from their attained marks
    
    for line in file_reader:
        student_name, student_gwa = line.strip().split(",")
        class_record_dict[student_name] = student_gwa
        print (class_record_dict)
    
    # Determine the highest and lowest grade that a student can recieve
    
    
    
    # Have the program read each gwa and compare it with the highest grade level a student can recieve.   
    

         # Print the name and the grade of the student with the highest grade and highest GWA.
         # Hint: The highest grade presented should be Joshua Adrian Cabanatuan - 1.53
        