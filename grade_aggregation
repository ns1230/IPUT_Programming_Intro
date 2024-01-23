#Collects and returns student data.
def get_student_data():
    students = []
    while input("データを追加しますか？[y/n] ") == 'y':
        student_name = input("Name: ")
        scores = [int(input("Score: ")) for _ in range(4)]
        average_score = round(sum(scores) / 4, 1)
        student_data = {
            "name": student_name,
            "average": average_score,
            "highest": max(scores),
            "lowest": min(scores)
        }
        students.append(student_data)
    return students

# Get and process student data
student_grades = get_student_data()

# Displaying the data
for student in student_grades:
    print(f"{student['name']} - 平均: {student['average']} 最高: {student['highest']} 最低: {student['lowest']}")
