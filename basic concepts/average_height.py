students_heights = input(
    "Input a list of students heights separated by a space \n").split()

# We can use split to convert a input with multiple number or letter can be converted into a list
# we can use split as split(", ") to convert numbers which are separated by comma and a space

number_of_students = len(students_heights)
# sum_of_heights = 0

for n in range(0, number_of_students):
    students_heights[n] = int(students_heights[n])

sum_of_heights = sum(students_heights)
average_of_heights = round(sum_of_heights / number_of_students)

print(f"Average of all the heights is {average_of_heights}")
