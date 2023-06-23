import student
from datetime import datetime

def write_to_error_log(message):
    try:
        #open log file
        log_file = open("error_log.txt", "a")
        #write error message to log file
        log_file.write(f"{datetime.now()}: {message}\n")
        #close log file
        log_file.close()
    except Exception as err:
        print(err)
        return
    return

def main():
    try:
        list_of_students = []

        #create a file handler
        file = open("students.csv", "r")

        #create variable to keep track of line in file that we are reading
        line_number = 0
        #read file line by line in for loop
        for line_of_data in file:
            line_number += 1
            #skip first line in csv file
            if line_number == 1:
                continue
            #split the lineof data at the comma
            student_data = line_of_data.split(",")

            #handle errors in data format. line_of_data should have 6 items
            #if error in format then write a message to a log file
            if len(student_data) != 6:
                raise Exception(f"There is an error in your data file on line{line_number}")
            
            #get student data and create a student object for each student
            first_name = student_data[0]
            last_name = student_data[1]
            major = student_data[2]
            credit_hours = int(student_data[3])
            gpa = float(student_data[4])
            student_id = student_data[5].strip()

            new_student = student.Student(first_name, last_name, major, credit_hours, gpa, student_id)
            list_of_students.append(new_student)

    except Exception as err:
        print(err)

    for students in list_of_students:
        print()
        students.print_student_data()

    """"
    data_file = open("students.csv", "r")

    info = []

    for line in data_file:
        info = line.split(",")
        a_student = student.Student(info[0], info[1], info[2], int(info[3]), float(info[4]), info[5])
        a_student.print_student_data()
    """
main()