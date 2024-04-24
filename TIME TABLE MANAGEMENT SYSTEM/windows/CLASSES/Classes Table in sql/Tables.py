import mysql.connector
mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='lenovo@#021',
    database='school')
mycursor=mydb.cursor()
a = "Create Table CLASS1(DAY varchar(30),Period1 varchar(30),Period2 varchar(30),Period3 varchar(30),\
Period4 varchar(30),Period5 varchar(30),Period6 varchar(30),Period7 varchar(30),Period8 varchar(30))"
b = "Create Table CLASS2(DAY varchar(30),Period1 varchar(30),Period2 varchar(30),Period3 varchar(30),\
Period4 varchar(30),Period5 varchar(30),Period6 varchar(30),Period7 varchar(30),Period8 varchar(30))"
c = "Create Table CLASS3(DAY varchar(30),Period1 varchar(30),Period2 varchar(30),Period3 varchar(30),\
Period4 varchar(30),Period5 varchar(30),Period6 varchar(30),Period7 varchar(30),Period8 varchar(30))"
d = "Create Table CLASS4(DAY varchar(30),Period1 varchar(30),Period2 varchar(30),Period3 varchar(30),\
Period4 varchar(30),Period5 varchar(30),Period6 varchar(30),Period7 varchar(30),Period8 varchar(30))"
e = "Create Table CLASS5(DAY varchar(30),Period1 varchar(30),Period2 varchar(30),Period3 varchar(30),\
Period4 varchar(30),Period5 varchar(30),Period6 varchar(30),Period7 varchar(30),Period8 varchar(30))"
f = "Create Table CLASS6(DAY varchar(30),Period1 varchar(30),Period2 varchar(30),Period3 varchar(30),\
Period4 varchar(30),Period5 varchar(30),Period6 varchar(30),Period7 varchar(30),Period8 varchar(30))"
g = "Create Table CLASS7(DAY varchar(30),Period1 varchar(30),Period2 varchar(30),Period3 varchar(30),\
Period4 varchar(30),Period5 varchar(30),Period6 varchar(30),Period7 varchar(30),Period8 varchar(30))"
h = "Create Table CLASS8(DAY varchar(30),Period1 varchar(30),Period2 varchar(30),Period3 varchar(30),\
Period4 varchar(30),Period5 varchar(30),Period6 varchar(30),Period7 varchar(30),Period8 varchar(30))"
i = "Create Table CLASS9(DAY varchar(30),Period1 varchar(30),Period2 varchar(30),Period3 varchar(30),\
Period4 varchar(30),Period5 varchar(30),Period6 varchar(30),Period7 varchar(30),Period8 varchar(30))"
j = "Create Table CLASS10(DAY varchar(30),Period1 varchar(30),Period2 varchar(30),Period3 varchar(30),\
Period4 varchar(30),Period5 varchar(30),Period6 varchar(30),Period7 varchar(30),Period8 varchar(30))"
k = "Create Table CLASS11(DAY varchar(30),Period1 varchar(30),Period2 varchar(30),Period3 varchar(30),\
Period4 varchar(30),Period5 varchar(30),Period6 varchar(30),Period7 varchar(30),Period8 varchar(30))"
s = "Create Table CLASS12(DAY varchar(30),Period1 varchar(30),Period2 varchar(30),Period3 varchar(30),\
Period4 varchar(30),Period5 varchar(30),Period6 varchar(30),Period7 varchar(30),Period8 varchar(30))"
mycursor.execute(a)
mycursor.execute(b)
mycursor.execute(c)
mycursor.execute(d)
mycursor.execute(e)
mycursor.execute(f)
mycursor.execute(g)
mycursor.execute(h)
mycursor.execute(i)
mycursor.execute(j)
mycursor.execute(k)
mycursor.execute(s)
