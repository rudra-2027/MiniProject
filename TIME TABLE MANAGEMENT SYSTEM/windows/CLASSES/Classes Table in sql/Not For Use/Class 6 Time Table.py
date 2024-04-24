import mysql.connector
mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='lenovo@#021',
    database='school')
mycursor=mydb.cursor()
s ='insert into CLASS1(day,period1,period2,period3,period4,period5,period6,period7,period8) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
val=[('Monday',    'English', 'Maths',      'Science',     'Hindi',      '',           '',          'SST',      'Sanskrit'),
     ('Tuesday',   'English', 'Maths',      'Science',     'Hindi',      'PHE',        'Library',   'SST',      'Sanskrit'),
     ('Wednesday', 'English', '',           'Science',     'Hindi',      'Computer',   '',          'SST',      'Sanskrit'),
     ('Thursday',  'English', 'Computer',   'Science',     'Hindi',      'Maths',      'Maths',     'SST',      'Library'),
     ('Friday',    'English', 'AE',         'Science',     'Hindi',      'Maths',      'PHE',       'SST',      'SST'),
     ('Saturday',  'English', 'Hindi',      'Science',     'Computer',   'Maths',      'Maths',     'CCA',      'CCA'),
      ]
mycursor.executemany(s,val)
mydb.commit()
