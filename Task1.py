class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def __str__(self):
        result = f' Имя: {self.name}\n'\
              f' Фамилия: {self.surname}\n'\
              f' Средняя оценка за домашние задания: {self.__get_average_score():,.2f}\n'\
              f' Курсы в процессе изучения: { ", ".join(self.courses_in_progress)}\n'\
              f' Завершенные курсы: {", ".join(self.finished_courses)}\n'
        return result

    def __get_average_score(self):
        """расчет средней оценки ДЗ студента"""
        result = []
        for grade in self.grades.values():
            result.extend(grade)
        return sum(result)/len(result)

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_hw(self, lecturer, course, grade):
        if grade > 10:
            grade = 10
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Not a Student!')
            return
        return self.__get_average_score() < other.__get_average_score()

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        res = f' Имя: {self.name}\n'\
              f' Фамилия: {self.surname}\n'\
              f' Средняя оценка за лекции: {self.__get_average_score():,.2f}\n'
        return res

    def __get_average_score(self):
        """расчет среднего балла оценок преподавателя"""
        result = []
        for grade in self.grades.values():
            result.extend(grade)
        return sum(result)/len(result)

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Not a Lecturer!')
            return
        return self.__get_average_score() < other.__get_average_score()

class Reviewer (Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if grade > 10:
            grade = 10
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f' Имя: {self.name}\n Фамилия: {self.surname}\n'
        return res

def get_student_avg_score(students, course):
    """Рассчет средней оценки за ДЗ студентов на курсе
        аргументы: список студентов, название курса """
    result = 0
    for student in students:
        if course in student.courses_in_progress:
            grades = student.grades[course]
            result += sum(grades)/len(grades)
    return f' Средняя оценка студентов курса {course} за домашние задания: {result:,.2f}\n'

def get_lecturer_avg_score(lecturers, course):
    """Рассчет средней оценки за лекции преподавателей курса
         аргументы: список преподавателей, название курса"""
    result = 0
    for lecturer in lecturers:
        if course in lecturer.courses_attached:
            grades = lecturer.grades[course]
            result += sum(grades)/len(grades)
    return f' Средняя оценка преподавателей за лекции курса {course}: {result:,.2f}\n'

# set values
reviewer1 = Reviewer('Matthew', 'Stone')
reviewer1.courses_attached += ['Python']
reviewer1.courses_attached += ['Git']

lecturer1 = Lecturer('John', 'Carter')
lecturer1.courses_attached += ['Python']

lecturer2 = Lecturer('Jack', 'Russell')
lecturer2.courses_attached += ['Git']

student1 = Student('Eric', 'Cartman', 'm')
student1.courses_in_progress += ['Python']
student1.courses_in_progress += ['Git']
student1.finished_courses += ['Introduction to programming']

reviewer1.rate_hw(student1, 'Python', 10)
reviewer1.rate_hw(student1, 'Python', 15)
reviewer1.rate_hw(student1, 'Python', 8)
reviewer1.rate_hw(student1, 'Git', 8)
reviewer1.rate_hw(student1, 'Git', 9)
reviewer1.rate_hw(student1, 'Git', 6)

student1.rate_hw(lecturer1, 'Python', 12)
student1.rate_hw(lecturer1, 'Python', 8)
student1.rate_hw(lecturer1, 'Python', 5)
student1.rate_hw(lecturer2, 'Git', 10)
student1.rate_hw(lecturer2, 'Git', 8)

student2 = Student('Kyle', 'Broflovski', 'm')
student2.courses_in_progress += ['Python']
student2.courses_in_progress += ['Git']
student2.finished_courses += ['Introduction to programming']

reviewer1.rate_hw(student2, 'Python', 8)
reviewer1.rate_hw(student2, 'Python', 9)
reviewer1.rate_hw(student2, 'Python', 10)
reviewer1.rate_hw(student2, 'Git', 7)
reviewer1.rate_hw(student2, 'Git', 10)
reviewer1.rate_hw(student2, 'Git', 10)

student2.rate_hw(lecturer1, 'Python', 7)
student2.rate_hw(lecturer1, 'Python', 8)
student2.rate_hw(lecturer1, 'Python', 5)
student2.rate_hw(lecturer2, 'Git', 10)
student2.rate_hw(lecturer2, 'Git', 6)


def main():

    print(reviewer1)

    print(student1)
    print(student2)

    print(lecturer1)
    print(lecturer2)

    students = []
    students.append(student1)
    students.append(student2)

    lecturers = []
    lecturers.append(lecturer1)
    lecturers.append(lecturer2)

    print(get_student_avg_score(students, 'Python'))
    print(get_student_avg_score(students, 'Git'))

    print(get_lecturer_avg_score(lecturers, 'Python'))
    print(get_lecturer_avg_score(lecturers, 'Git'))

    print(f' Успеваемость student1 < student2: {student1 < student2}')
    print(f' Рейтинг lecturer1 > lecturer2: {lecturer1 > lecturer2}')

main()