import mysql.connector
mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='lenovo@#021',
    database='school')
mycursor=mydb.cursor()
s = "Create Table CLASS11(DAY varchar(30),Period1 varchar(30),Period2 varchar(30),Period3 varchar(30),\
Period4 varchar(30),Period5 varchar(30),Period6 varchar(30),Period7 varchar(30),Period8 varchar(30))"
mycursor.execute(s)
