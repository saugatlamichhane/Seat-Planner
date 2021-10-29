# TODO Add a README in github project
# TODO Learn about licenses
# TODO Add a licence in github project

from School import School
from Grade import Grade
from Room import Room

# Create object "school" and set the attributes from user input.
school_name = input("Enter the name of school:")
school_address = input("Enter the address of school:")
least_grade = input("Grades start from:")
highest_grade = input("Upto which grade: ")
school = School(school_name, school_address, least_grade, highest_grade)

# Take the examination infos as user input.
examination_name = input("Enter the title of examination:")
examination_year = input("Enter the examination year:")

# Add the first room to roomList
current_room = room(1)
# TODO modify in order to adapt this program for exam rooms with unequal number of rooms in door and corner side
no_of_desks_in_each_side = int(input("How many desks are there in each side of Room No. 1?"))
# Add each seat to emptySeats
for i in range(1, no_of_desks_in_each_side * 6 + 1):
    current_room.append("SN" + format_number(1) + format_number(i))

# Starting from highestGrade, allot seats for each student in each grade
grade_sn_counter = school.highestGrade
while grade_sn_counter + 1 > school.leastGrade:
    allot_seat(grade_sn_counter)
    grade_sn_counter -= 1

# TODO Create PDF file.

# Allots seat for each student of the grade
def allot_seat(grade_sn):
    # Create a grade object
    grade = Grade(grade_sn)
    # For creating a list of sections, taking user input
    no_of_sections = input("How many sections are there in grade " + grade_sn + "?")
    sections_string = input("What are those sections?(Use space as separator between sections.)")
    # Creates a list of sections
    sections = sections_string.split()
    for i in range(len(sections) + 1):
        # Capitalizing the first letter of the word
        current_section = sections[i].capitalize()
        # Taking the first letter of the capitalized word and replacing the corresponding section in the sections list
        sections[i] = current_section[0]
    for section in sections:
        no_of_students = input("How many students are there in " + grade.gradeSN + "'" + section +"'?")
        for j in range(1, no_of_students + 1):
            # Assigning symbol number to each student
            student = format_number(grade.gradeSN) + format_number(j) + "'" + section +"'"
            # Adding each student to the students list of the corresponding grade
            grade.students.append(student)
    for student in students:
        # Check if room is available and place the student in the first available seat.
        # TODO allot the seats for random student not in increasing order of Roll No.
        # Remove that seat form "emptySeats" and remove that student from "nonAllotedStds".
        # TODO check if seat is available and allot the appropriate seat for him/her.

#Returns two-digit number as string
def format_number(number):
    if number < 10:
        return "0" + str(number)
    else:
        return str(number)