import mysql.connector
mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='lenovo@#021',
    database='school')
mycursor=mydb.cursor()
s ='insert into CLASS8(day,period1,period2,period3,period4,period5,period6,period7,period8) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
val=[('Monday',    'Hindi', 'Science',   'English',  'AE',       'SST',       'Maths',   'Music',   'PHE'),
     ('Tuesday',   'Hindi', 'Computer',  'English',  'Science',  'SST',       'Maths',   'Maths',   'Library'),
     ('Wednesday', 'Hindi', 'Sanskrit',  'Maths',    'SST',      'Sanskrit',  'Maths',   '',     'Music'),
     ('Thursday',  'Hindi', 'Science',   'English',  'SST',      'Sanskrit',  'Yoga',    'Maths',   'PHE'),
     ('Friday',    'Hindi', 'Library',   'English',  'SST',      'Science',   'Maths',   'AE',      'Science'),
     ('Saturday',  'Hindi', 'English',   'Science',  'SST',      'Computer',  'English', 'CCA',     'CCA'),
      ]
mycursor.executemany(s,val)
mydb.commit()
