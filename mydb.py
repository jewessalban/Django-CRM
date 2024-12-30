import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'jewess2006'

)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE jewess")

print("All Done!")