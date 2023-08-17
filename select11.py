import mysql.connector


database =mysql.connector.connect(
  host ="localhost",
  user ="root",
  passwd ="kishore29@",
  auth_plugin='mysql_native_password'
)

# preparing a cursor object
cursorObject = database.cursor()

# query = "SELECT NAME, ROLL FROM STUDENT"
query = "show databases;"
cursorObject.execute(query)

myresult = cursorObject.fetchall()

for x in myresult:
    print(x)

# disconnecting from server
database.close()