import mysql.connector
mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='lenovo@#021',
    database='school')
mycursor=mydb.cursor()
s ='insert into CLASS9(day,period1,period2,period3,period4,period5,period6,period7,period8) values(%s,%s,%s,%s,%s,%s\
,%s,%s,%s)'
val=[('Monday',    'SST', 'Hindi',   'Maths',    'Physics',  'PHE',    'Chemistry',  'English',     'English'),
     ('Tuesday',   'SST', 'SST',     'Computer', 'Physics',  'Hindi',  'Maths',      'Maths',       'Hindi'),
     ('Wednesday', 'SST', 'Physics', 'Biology',  'Computer', 'Hindi',  'English',    'PHE',         'English'),
     ('Thursday',  'SST', 'Yoga',    'Biology',  'Computer', 'Hindi',  'Maths',      'AE',          'English'),
     ('Friday',    'SST', 'Music',   'WE',       'Maths',    'Maths',  'English',    'Chemistry',   'Hindi'),
     ('Saturday',  'SST', 'Library', 'English',  'Maths',    'Hindi',  'Computer',   'CCA',         'CCA'),
      ]
mycursor.executemany(s,val)
mydb.commit()
