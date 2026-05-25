#Converting List to a Dictionary

students = [

[1, "John Doe", 'V'],
[2, "David Monroe", 'VI'],
[3, "Jennifer Lowrence", 'V'],
[4, "Peter Gold", 'VII'],
[5, "Thomas Edison", 'VI'],
]

print(students)

def convert_to_dict(students):
    student_dict = {}
    for student in students:
        student_dict[student[0]] = student[1]
    return student_dict

print("Original List : ", students)
print("Converted Dictionary : ", convert_to_dict(students))
        