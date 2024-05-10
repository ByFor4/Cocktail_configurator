import mysql.connector

mydb = mysql.connector.connect(
    host = "127.0.0.1",
    port = "3306",
)

mycursor = mydb.cursor()

mycursor.execute("SHOW DATABASES")

for x in mycursor:
    print(x)
print("123")