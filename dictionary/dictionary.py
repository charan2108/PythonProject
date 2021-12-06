# student_grades = {'harry': 9.8, 'potter': 9.6, 'hermonie': 9.7}
# mySum = sum(student_grades.values())
# length = len(student_grades)
# result = mySum / length
# print(result)


# day_temperatures = {'mornings': 12.5, 'noon': 20.0, 'evening': 30}
# print(day_temperatures)
# print(day_temperatures['mornings'])

# day_temperatures = {'morning': (15.5, 20.5, 12.9), 'noon': (
#     20.5, 25.5, 18.9), 'evening': (15.5, 20.5, 12.9)}

# Looping trough dictionary
student_grades = {'harry': 9.8, 'potter': 9.6, 'hermonie': 9.7}

for grades in student_grades.items():
    print(grades)

phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}

for k,v in phone_numbers.items():
    print("{} {}".format(k,v))

phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}

for value in phone_numbers.values():
    print(value.replace("+", "00"))
