import mysql.connector
mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='lenovo@#021',
    database='school')
mycursor=mydb.cursor()
s ='insert into CLASS11(day,period1,period2,period3,period4,period5,period6,period7,period8) values(%s,%s,%s,%s,%s,%s,\
%s,%s,%s)'
val=[('Monday',    'Chemistry', 'English', 'C.S/Hindi',  'Yoga',      'Maths/Bio',  'Maths/Bio', 'C.S/Hindi', 'C.S/Hindi'),
     ('Tuesday',   'Maths/Bio', 'English', 'C.S/Hindi',  'Chemistry', 'Yoga',       'GS',        'Physics',   'Maths/Bio'),
     ('Wednesday', 'Chemistry', 'English', 'C.S/Hindi',  'Maths/Bio', 'Physics',    'PHE',       'PHY/CHE',   'PHY/CHE'),
     ('Thursday',  'Physics',   'English', 'C.S/Hindi',  'Maths/Bio', 'Chemistry',  'Library',   'PHY/CHE',   'PHY/CHE'),
     ('Friday',    'Chemistry', 'English', 'Maths/Bio',  'Physics',   'C.S/Hindi',  'C.S/Hindi', 'Physics',   'PHE'),
     ('Saturday',  'Chemistry', 'English', 'C.S/Hindi',  'Physics',   'Maths/Bio',  'Maths/Bio', 'CCA',       'CCA'),
      ]
mycursor.executemany(s,val)
mydb.commit()
