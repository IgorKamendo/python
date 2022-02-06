import sqlite3

conn = sqlite3.connect('db1.sqlite')

cursor = conn.cursor()

# cursor.execute("CREATE TABLE Students (id int, name Varchar(32), surname Varchar (32), age int, city Varchar (
# 32))") cursor.execute("CREATE TABLE Courses (id int, name Varchar(32), time_start Varchar(32), time_end Varchar(
# 32))") cursor.execute("CREATE TABLE Students_courses (student_id int, course_id int)") cursor.execute('''INSERT
# INTO Courses (id,name,time_start,time_end) VALUES (1,'python','21.07.21','21.08.21')''') cursor.execute('''INSERT
# INTO Courses (id,name,time_start,time_end) VALUES (2,'java','13.07.21','16.08.21')''') cursor.execute('''INSERT
# INTO Students (id,name,surname,age,city) VALUES (1,'Max','Brooks',24,'Spb')''') cursor.executemany('INSERT INTO
# Students VALUES(?,?,?,?,?)',[(2, 'John', 'Stones', 15, 'Spb'), (3, 'Andy', 'Wings', 45, 'Manhester'),(4, 'Kate',
# 'Brooks', 34, 'Spb')]) cursor.executemany('INSERT INTO Students_courses VALUES(?,?)', [(1, 1), (2, 1), (3, 1), (4,
# 2)])

cursor.execute('SELECT Students.name, Students.surname FROM Students WHERE age > 30')
print("Все студенты старше 30 лет:", cursor.fetchall())

cursor.execute('SELECT Students.name, Students.surname FROM Students_courses JOIN Students ON '
               'Students_courses.student_id = Students.id WHERE course_id = 1')
print("Все студенты, которые проходят курс по python:", cursor.fetchall())

cursor.execute('SELECT Students.name, Students.surname FROM Students_courses JOIN Students ON '
               'Students_courses.student_id = Students.id WHERE course_id = 1 AND Students.city = "Spb"')
print("Все студенты, которые проходят курс по python и из СПб:", cursor.fetchall())

#conn.commit()
conn.close()
