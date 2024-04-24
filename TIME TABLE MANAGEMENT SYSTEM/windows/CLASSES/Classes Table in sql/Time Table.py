import mysql.connector
mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='lenovo@#021',
    database='school')
mycursor=mydb.cursor()
a ='insert into CLASS6(day,period1,period2,period3,period4,period5,period6,period7,period8) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
val1=[('Monday',    'English', 'Maths',      'Science',     'Hindi',      '',           '',          'SST',      'Sanskrit'),
     ('Tuesday',   'English', 'Maths',      'Science',     'Hindi',      'PHE',        'Library',   'SST',      'Sanskrit'),
     ('Wednesday', 'English', '',           'Science',     'Hindi',      'Computer',   '',          'SST',      'Sanskrit'),
     ('Thursday',  'English', 'Computer',   'Science',     'Hindi',      'Maths',      'Maths',     'SST',      'Library'),
     ('Friday',    'English', 'AE',         'Science',     'Hindi',      'Maths',      'PHE',       'SST',      'SST'),
     ('Saturday',  'English', 'Hindi',      'Science',     'Computer',   'Maths',      'Maths',     'CCA',      'CCA'),
      ]
b ='insert into CLASS7(day,period1,period2,period3,period4,period5,period6,period7,period8) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
val2=[('Monday',    'Maths', '',          'Hindi',     'English',      'Science',    'SST',   'AE',        'Library'),
     ('Tuesday',   'Maths', 'Sanskrit',  'Hindi',     'English',      'Science',    'SST',   'AE',        'WE'),
     ('Wednesday', 'Maths', 'Computer',  'Sanskrit',  'Science',      'English',    'SST',   'Hindi',     'Library'),
     ('Thursday',  'Maths', 'PHE',       'Hindi',     'Science',      'English',    'SST',   'English',   'Sanskrit'),
     ('Friday',    'Maths', 'PHE',       'Maths',     'Science',      'English',    'SST',   'Hindi',     'Hindi'),
     ('Saturday',  'Maths', 'Computer',  'Music',     'Science',      'English',    'SST',   'CCA',       'CCA'),
      ]
c ='insert into CLASS8(day,period1,period2,period3,period4,period5,period6,period7,period8) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
val3=[('Monday',    'Hindi', 'Science',   'English',  'AE',       'SST',       'Maths',   'Music',   'PHE'),
     ('Tuesday',   'Hindi', 'Computer',  'English',  'Science',  'SST',       'Maths',   'Maths',   'Library'),
     ('Wednesday', 'Hindi', 'Sanskrit',  'Maths',    'SST',      'Sanskrit',  'Maths',   '',     'Music'),
     ('Thursday',  'Hindi', 'Science',   'English',  'SST',      'Sanskrit',  'Yoga',    'Maths',   'PHE'),
     ('Friday',    'Hindi', 'Library',   'English',  'SST',      'Science',   'Maths',   'AE',      'Science'),
     ('Saturday',  'Hindi', 'English',   'Science',  'SST',      'Computer',  'English', 'CCA',     'CCA'),
      ]

d ='insert into CLASS9(day,period1,period2,period3,period4,period5,period6,period7,period8) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
val4=[('Monday',    'SST', 'Hindi',   'Maths',    'Physics',  'PHE',    'Chemistry',  'English',     'English'),
     ('Tuesday',   'SST', 'SST',     'Computer', 'Physics',  'Hindi',  'Maths',      'Maths',       'Hindi'),
     ('Wednesday', 'SST', 'Physics', 'Biology',  'Computer', 'Hindi',  'English',    'PHE',         'English'),
     ('Thursday',  'SST', 'Yoga',    'Biology',  'Computer', 'Hindi',  'Maths',      'AE',          'English'),
     ('Friday',    'SST', 'Music',   'WE',       'Maths',    'Maths',  'English',    'Chemistry',   'Hindi'),
     ('Saturday',  'SST', 'Library', 'English',  'Maths',    'Hindi',  'Computer',   'CCA',         'CCA'),
      ]

e ='insert into CLASS10(day,period1,period2,period3,period4,period5,period6,period7,period8) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
val5=[('Monday',    'English', 'SST',   'Yoga',       'Chemistry',   'Hindi',    'Hindi',  'Maths',  'Maths'),
     ('Tuesday',   'English', 'AE',    'Chemistry',  'Maths',       'Computer', 'Hindi',  'PHE',    'SST'),
     ('Wednesday', 'English', 'Maths', 'SST',        'Physics',     'Biology',  'Hindi',  'Music',  'English'),
     ('Thursday',  'English', 'Maths', 'SST',        'Physics',     'Computer', 'Hindi',  'Yoga',   'SST'),
     ('Friday',    'English', 'Maths', 'SST',        'Biology',     'Library',  'Hindi',  'PHE',    'Com'),
     ('Saturday',  'English', 'Maths', 'SST',        'Biology',     'Computer', 'Hindi',  'CCA',    'CCA'),
      ]
f ='insert into CLASS11(day,period1,period2,period3,period4,period5,period6,period7,period8) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
val6=[('Monday',    'Chemistry', 'English', 'C.S/Hindi',  'Yoga',      'Maths/Bio',  'Maths/Bio', 'C.S/Hindi', 'C.S/Hindi'),
     ('Tuesday',   'Maths/Bio', 'English', 'C.S/Hindi',  'Chemistry', 'Yoga',       'GS',        'Physics',   'Maths/Bio'),
     ('Wednesday', 'Chemistry', 'English', 'C.S/Hindi',  'Maths/Bio', 'Physics',    'PHE',       'PHY/CHE',   'PHY/CHE'),
     ('Thursday',  'Physics',   'English', 'C.S/Hindi',  'Maths/Bio', 'Chemistry',  'Library',   'PHY/CHE',   'PHY/CHE'),
     ('Friday',    'Chemistry', 'English', 'Maths/Bio',  'Physics',   'C.S/Hindi',  'C.S/Hindi', 'Physics',   'PHE'),
     ('Saturday',  'Chemistry', 'English', 'C.S/Hindi',  'Physics',   'Maths/Bio',  'Maths/Bio', 'CCA',       'CCA'),
      ]
g ='insert into CLASS12(day,period1,period2,period3,period4,period5,period6,period7,period8) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
val7=[('Monday','Maths/Bio','Physics','Chemisrty','English','Physics','Physics','C.S/Hindi','C.S/Hindi'),
     ('Tuesday','C.S/Hindi','Maths/Bio','Maths/Bio','English','C.S/Hindi','C.S/Hindi','Physics','Physics'),
     ('Wednesday','Physics','Maths/Bio','Chemistry','PHE','English','Maths/Bio','Maths/Bio','C.S/Hindi'),
     ('Thursday','C.S/Hindi','Physics','Chemistry','English','Maths/Bio','Physics','G.A','Maths/Bio'),
     ('Friday','C.S/Hindi','Physics','Chemistry','PHE','Chemistry','Chemistry','Eglish','Library'),
     ('Saturday','Maths/Bio','C.S/Hindi','Chemistry','English','Chemistry','Chemistry','CCA','CCA'),
      ]

mycursor.executemany(a,val1)
mycursor.executemany(b,val2)
mycursor.executemany(c,val3)
mycursor.executemany(d,val4)
mycursor.executemany(e,val5)
mycursor.executemany(f,val6)
mycursor.executemany(g,val7)
mydb.commit()
