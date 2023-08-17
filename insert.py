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

sql = "INSERT INTO STUDENT (NAME, BRANCH, ROLL, SECTION, AGE)\
VALUES (%s, %s, %s, %s, %s)"
val = [("kishore", "MEC", "98", "A", "18"),
       ("praveen", "MEC", "99", "A", "18"),
       ("Rohan", "MAE", "43", "B", "20"),
       ("Amit", "ECE", "24", "A", "21"),
       ("Anil", "MAE", "45", "B", "20"),
       ("Megha", "ECE", "55", "A", "22"),
       ("Sita", "CSE", "95", "A", "19")]

cursorObject.executemany(sql, val)
database.commit()

# disconnecting from server
database.close()