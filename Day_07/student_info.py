classroom = []

for i in range(2):
    student = {
        "name": input("Enter your name: "),
        "age": int(input("Enter your age: ")),
        "language": input("Enter your favorite programming language: ")
    }
    classroom.append(student)

print("\n ---Classroom Information---")
for student in classroom:
    print(
        f"Name: {student['name']}\nAge: {student['age']}\nFavorite Programming Language: {student['language']}")
    print("-----------------------------")
