import mysql.connector.python
mydb=mysql.connector.connect(host='127.0.0.1',port='3306',auth_plugin='mysql_native_password',user='root',passwd='user@12345')
if mydb:
    print("Connection Successful")
else:
    print("Connection failed")