import mysql.connector
mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='lenovo@#021',
    database='school')
mycursor=mydb.cursor()
s ='insert into CLASS10(day,period1,period2,period3,period4,period5,period6,period7,period8) values(%s,%s,%s,%s,%s,%s,%s,\
%s,%s)'
val=[('Monday',    'English', 'SST',   'Yoga',       'Chemistry',   'Hindi',    'Hindi',  'Maths',  'Maths'),
     ('Tuesday',   'English', 'AE',    'Chemistry',  'Maths',       'Computer', 'Hindi',  'PHE',    'SST'),
     ('Wednesday', 'English', 'Maths', 'SST',        'Physics',     'Biology',  'Hindi',  'Music',  'English'),
     ('Thursday',  'English', 'Maths', 'SST',        'Physics',     'Computer', 'Hindi',  'Yoga',   'SST'),
     ('Friday',    'English', 'Maths', 'SST',        'Biology',     'Library',  'Hindi',  'PHE',    'Com'),
     ('Saturday',  'English', 'Maths', 'SST',        'Biology',     'Computer', 'Hindi',  'CCA',    'CCA'),
      ]
mycursor.executemany(s,val)
mydb.commit()
