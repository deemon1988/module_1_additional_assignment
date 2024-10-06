#  Дополнительное практическое задание по модулю: "Базовые структуры данных."
from typing import final

grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
list_students = list(students)
list_students.sort()
print(list_students)

print(list_students[0])

score_Aaron = sum(grades[0]) / len(grades[0])
score_Bilbo = sum(grades[1]) / len(grades[1])
score_Johnny = sum(grades[2]) / len(grades[2])
score_Khendrik = sum(grades[3]) / len(grades[3])
score_Steve = sum(grades[4]) / len(grades[4])
print(score_Aaron, score_Bilbo, score_Johnny, score_Khendrik, score_Steve)
dict_score = {list_students[0]: score_Aaron}
print(dict_score)

for student_grade in grades:
    avg_grade = sum(student_grade) / len(student_grade)
    print(round(avg_grade,1))


def nothing():
    pass
# def find_average1(*, list_score: list) -> float:
#
#     return sum(list_score)/len(list_score)
#
# find_average1(list_score=grades)
