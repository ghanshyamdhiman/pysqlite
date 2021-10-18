import mysql.connector

rm_host = 'localhost'
#rm_host = '192.168.0.25:3306'

mydb = mysql.connector.connect(
  host=rm_host,
  user="user1",
  password="user123",
  database="testdb1"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM products")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
