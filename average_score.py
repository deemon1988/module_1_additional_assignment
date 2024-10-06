#  Дополнительное практическое задание по модулю: "Базовые структуры данных."
from typing import final

grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

list_students = list(students)
list_students.sort()
print(list_students)

avg_list_grades = []
for student_grade in grades:
    avg_grade = sum(student_grade) / len(student_grade)
    avg_list_grades.append(round(avg_grade,1))

print(avg_list_grades)


dict_students ={}
for i in range(len(list_students)):
    dict_students[list_students[i]] = avg_list_grades[i]

print(dict_students)

def nothing():
    pass
