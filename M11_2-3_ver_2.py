import unittest

from peewee import *

conn = SqliteDatabase('db2.sqlite')


class Students(Model):
    id_students = PrimaryKeyField(column_name='id_students')
    name = CharField(column_name='name')
    surname = CharField(column_name='surname')
    age = IntegerField(column_name='age')
    city = CharField(column_name='city')

    class Meta:
        database = conn


class Courses(Model):
    id_courses = PrimaryKeyField(column_name='id_courses')
    name = CharField(column_name='name')
    time_start = CharField(column_name='time_start')
    time_end = CharField(column_name='time_end')

    class Meta:
        database = conn


class Students_courses(Model):
    student_id = ForeignKeyField(Students, to_field='id', column_name='students_id')
    course_id = ForeignKeyField(Courses, to_field='id', column_name='course_id')

    class Meta:
        database = conn

s1 = [{'id': 1, 'name': 'Max', 'surname': 'Brooks', 'age': 24, 'city': 'Spb'},
      {'id': 2, 'name': 'John', 'surname': 'Stones', 'age': 15, 'city': 'Spb'},
      {'id': 3, 'name': 'Andy', 'surname': 'Wings', 'age': 45, 'city': 'Manhester'},
      {'id': 4, 'name': 'Kate', 'surname': 'Brooks', 'age': 34, 'city': 'Spb'}]
#Students.insert_many(s1).execute()

c1 = [{'id': 1, 'name': 'python', 'time_start': '21.07.21', 'time_end': '21.08.21'},
      {'id': 2, 'name': 'java', 'time_start': '13.07.21', 'time_end': '16.08.21'}]
#Courses.insert_many(c1).execute()

s_c1 = [{'student_id': 1, 'course_id': 1},
        {'student_id': 2, 'course_id': 1},
        {'student_id': 3, 'course_id': 1},
        {'student_id': 4, 'course_id': 2}]
#Students_courses.insert_many(s_c1).execute()

def add_students(id, name, surname, age, city, data):
    students = {'id': id, 'name': name, 'surname': surname, 'age': age, 'city': city}
    if students not in s1:
        Students.insert_many(s1).execute()
        return True
    return False

class Test(unittest.TestCase):

    def test_new_students(self):
        self.assertTrue(add_students(2, 'Tom', 'Gun', 25, 'Spb'))

    def test_existing_students(self):
        add_students(2, 'Tom', 'Gun', 25, 'Spb')
        self.assertFalse(add_students(2, 'Tom', 'Gun', 25, 'Spb'))

if __name__ == '__main__':
    unittest.main()
