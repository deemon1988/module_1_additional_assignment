#  Дополнительное практическое задание по модулю: "Базовые структуры данных."

grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}


def complete_dict(*, grades: list, students: set) -> dict[str, float]:
    list_students = list(students)
    list_students.sort()
    list_avg_grades = []
    for student_grade in grades:
        avg_grade = sum(student_grade) / len(student_grade)
        list_avg_grades.append(round(avg_grade, 1))

    dict_ = {}
    for i in range(len(list_students)):
        dict_[list_students[i]] = list_avg_grades[i]

    return dict_

dict_students = complete_dict(grades=grades, students=students)
print('Словарь средних оценок студентов:', dict_students)



def nothing():
    pass
