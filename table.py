import mysql.connector
#ALTER USER 'root'@'localhost' IDENTIFIED BY 'password' PASSWORD EXPIRE NEVER;
#ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'kishore29@'
database=mysql.connector.connect(
    host="localhost",
    user = "root ",
    passwd ="kishore29@",
    auth_plugin="mysql_native_password",
    database="besant10"
)

cursorObject= database.cursor()
studentRecord="""CREATE TABLE STUDENT(
              NAME VARCHAR(20) NOT NULL,
              BRANCH VARCHAR(50),
              ROLL INT NOT NULL,
              SECTION VARCHAR(5),
              AGE INT
              )"""
cursorObject.execute(studentRecord)
database.close()