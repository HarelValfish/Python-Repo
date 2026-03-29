# #1
# friend_ages = {
#     "Rolf": 24,
#     "Adam": 30,
#     "Anne": 27
# }
# print(friend_ages["Anne"])

# #2
# friend_ages = {
#     "Rolf": 24,
#     "Adam": 30
# }
# friend_ages["Bob"] = 20
# print(friend_ages)

# #3
# friend_ages = {
#     "Rolf": 24,
#     "Adam": 30
# }
# friend_ages["Adam"] = 40
# print(friend_ages)

# #4
# student_attendance = {
#     "Rolf": 96,
#     "Bob": 80,
#     "Anne": 100
# }
# if "Bob" in student_attendance:
#     print("Bob attended")

# #5
# student_attendance = {
#     "Rolf": 96,
#     "Bob": 80
# }
# for student in student_attendance:
#     print(student)

# #6
# student_attendance = {
#     "Rolf": 96,
#     "Bob": 80
# }
# for student in student_attendance:
#     print(f"{student} {student_attendance[student]}")

# #7
# student_attendance = {
#     "Rolf": 96,
#     "Bob": 80
# }
# for student, attendance in student_attendance.items():
#     print(f"{student} {attendance}")

# #8
# student_attendance = {
#     "Rolf": 100,
#     "Bob": 80,
#     "Anne": 60
# }
# total = 0
# students = 0
# for student in student_attendance:
#     students += 1
#     total = total + student_attendance[student]
# avg = total / students
# print(f"average grade is {avg}")

# #9
# friends = [
#     {"name": "Rolf", "age": 24},
#     {"name": "Adam", "age": 30}
# ]
# second_friend = friends[1]
# print(second_friend["name"])

# #10
# friends = [
#     {"name": "Rolf", "age": 24},
#     {"name": "Adam", "age": 30},
#     {"name": "Anne", "age": 27}
# ]

# result = []
# for friend in friends:
#     if friend["age"] > 25:
#         result.append(friend)
# print(result)