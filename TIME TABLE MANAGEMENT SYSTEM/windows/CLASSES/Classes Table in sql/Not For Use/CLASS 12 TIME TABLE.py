import mysql.connector
mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='lenovo@#021',
    database='school')
mycursor=mydb.cursor()
s ='insert into CLASS12(day,period1,period2,period3,period4,period5,period6,period7,period8) values(%s,%s,%s,%s,%s,%s,\
%s,%s,%s)'
val=[('Monday','Maths/Bio','Physics','Chemisrty','English','Physics','Physics','C.S/Hindi','C.S/Hindi'),
     ('Tuesday','C.S/Hindi','Maths/Bio','Maths/Bio','English','C.S/Hindi','C.S/Hindi','Physics','Physics'),
     ('Wednesday','Physics','Maths/Bio','Chemistry','PHE','English','Maths/Bio','Maths/Bio','C.S/Hindi'),
     ('Thursday','C.S/Hindi','Physics','Chemistry','English','Maths/Bio','Physics','G.A','Maths/Bio'),
     ('Friday','C.S/Hindi','Physics','Chemistry','PHE','Chemistry','Chemistry','Eglish','Library'),
     ('Saturday','Maths/Bio','C.S/Hindi','Chemistry','English','Chemistry','Chemistry','CCA','CCA'),
      ]
mycursor.executemany(s,val)
mydb.commit()
