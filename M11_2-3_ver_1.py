import unittest

def add_students(id_students, name, surname, age, city, data):
    students = {'id_students': id_students, 'name': name, 'surname': surname, 'age': age, 'city': city}
    if students not in data:
        data.append(students)
        return True
    return False


def add_courses(id_courses, name, time_start, time_end, data):
    courses = {'id_courses': id_courses, 'name': name, 'time_start': time_start, 'time_end': time_end}
    if courses not in data:
        data.append(courses)
        return True
    return False

def add_students_courses(students_id, courses_id, data):
    students_courses = {'students_id': students_id, 'courses_id': courses_id}
    if students_courses not in data:
        data.append(students_courses)
        return True
    return False

class Test(unittest.TestCase):

    def test_new_students(self):
        data = []
        self.assertTrue(add_students(1, 'Max', 'Brooks', 24, 'Spb', data))

    def test_existing_students(self):
        data = []
        add_students(1, 'Max', 'Brooks', 24, 'Spb', data)
        self.assertFalse(add_students(1, 'Max', 'Brooks', 24, 'Spb', data))

    def test_new_courses(self):
        data = []
        self.assertTrue(add_courses(1, 'python', '21.07.21', '21.08.21', data))

    def test_existing_courses(self):
        data = []
        add_courses(1, 'python', '21.07.21', '21.08.21', data)
        self.assertFalse(add_courses(1, 'python', '21.07.21', '21.08.21', data))

    def test_new_students_courses(self):
        data = []
        self.assertTrue(add_students_courses(1, 1, data))

    def test_existing_students_courses(self):
        data = []
        add_students_courses(1, 1, data)
        self.assertFalse(add_students_courses(1, 1, data))

if __name__ == '__main__':
    unittest.main()