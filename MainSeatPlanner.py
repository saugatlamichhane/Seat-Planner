from School import School

# Create object "school" and set the attributes from user input.
schoolName = input("Enter the name of school:")
schoolAddress = input("Enter the address of school:")
leastGrade = input("Grades start from:")
highestGrade = input("Upto which grade: ")
school = School(schoolName, schoolAddress, leastGrade, highestGrade)

# Take the examination infos as user input.
examinationName = input("Enter the title of examination:")
examinationYear = input("Enter the examination year:")

# Starting from highestGrade, create a "grade" object and set the attributes from user input.
grade = Grade()
# If there are no students left in nonAllotedStds, replace the object with the lower grade.
# If the current grade equals the least grade, proceed to the generation of pdf files.
# Check if room is available and place any random student from "nonAllotedStds" in the first available seat.
# If there are no availble seats in the room, go to next room and place him/her in the 1st available seat. 
# Remove that seat form "emptySeats" and remove that student from "nonAllotedStds".