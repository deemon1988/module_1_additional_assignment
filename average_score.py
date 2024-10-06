#  Дополнительное практическое задание по модулю: "Базовые структуры данных."
from typing import final

grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

list_students = list(students)
list_students.sort()
print(list_students)

def complete_dict(*, grades: list, students: list) -> dict[str, float]:
    list_avg_grades = []
    for student_grade in grades:
        avg_grade = sum(student_grade) / len(student_grade)
        list_avg_grades.append(round(avg_grade, 1))

    dict_students = {}
    for i in range(len(students)):
        dict_students[list_students[i]] = list_avg_grades[i]

    return dict_students


print('Словарь средних оценок студентов:', complete_dict(grades=grades, students=list_students))
print(type(complete_dict(grades=grades, students=list_students)))


def nothing():
    pass
