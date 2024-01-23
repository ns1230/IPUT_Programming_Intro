#Function to get and validate user input as an integer.
def get_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("数字を入力してください。")

# Get user inputs
attendance_count = get_input("出席回数：")
late_count = get_input("遅刻回数：")
absence_count = get_input("欠席回数：")
authorized_absence_count = get_input("公欠回数：")

# Calculate the total class number and adjusted attendance
total_classes = attendance_count + late_count + absence_count + authorized_absence_count
adjusted_attendance = attendance_count + late_count + authorized_absence_count - (late_count // 3)

# Calculate and display the attendance rate
attendance_rate = (adjusted_attendance / total_classes) * 100
print(f"出席率は{round(attendance_rate, 2)}％です")
