import mysql.connector

mydb = mysql.connector.connect(host='localhost', user='rogggiii', passwd='Messithegoat', database='accessnegative')

mycursor = mydb.cursor()

mycursor.execute('show tables')

for i in mycursor:
    print(i)




