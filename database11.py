import mysql.connector
#ALTER USER 'root'@'localhost' IDENTIFIED BY 'password' PASSWORD EXPIRE NEVER;
#ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'kishore29@'


database=mysql.connector.connect(
    host="localhost",
    user = "root ",
    passwd ="kishore29@",
    auth_plugin="mysql_native_password"
)

cursorObject = database.cursor()
cursorObject.execute("create DATABASE besant10;")
cursorObject.execute("show databases;")

myresult = cursorObject.fetchall()
print(myresult)

