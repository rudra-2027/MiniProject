import mysql.connector
mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='lenovo@#021',
    database='school')
mycursor=mydb.cursor()
s ='insert into CLASS7(day,period1,period2,period3,period4,period5,period6,period7,period8) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
val=[('Monday',    'Maths', '',          'Hindi',     'English',      'Science',    'SST',   'AE',        'Library'),
     ('Tuesday',   'Maths', 'Sanskrit',  'Hindi',     'English',      'Science',    'SST',   'AE',        'WE'),
     ('Wednesday', 'Maths', 'Computer',  'Sanskrit',  'Science',      'English',    'SST',   'Hindi',     'Library'),
     ('Thursday',  'Maths', 'PHE',       'Hindi',     'Science',      'English',    'SST',   'English',   'Sanskrit'),
     ('Friday',    'Maths', 'PHE',       'Maths',     'Science',      'English',    'SST',   'Hindi',     'Hindi'),
     ('Saturday',  'Maths', 'Computer',  'Music',     'Science',      'English',    'SST',   'CCA',       'CCA'),
      ]
mycursor.executemany(s,val)
mydb.commit()
