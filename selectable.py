import mysql.connector


database = mysql.connector.connect(
  host ="localhost",
  user ="root",
  passwd ="kishore29@",
  auth_plugin='mysql_native_password',
  database = "besant10"
)

# preparing a cursor object
cursorObject = database.cursor()

query = "DROP TABLE if exists Student;"
cursorObject.execute(query)


database.commit()

myresult = cursorObject.fetchall()
print(myresult)
for x in myresult:
	print(x)

# disconnecting from server
database.close()