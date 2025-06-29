import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", password="1234")
mycursor = mydb.cursor()

try:
    mycursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
except:
    print("Failed to connect to the Database")
else:
    print("Database 'alx_book_store' created successfully!")
finally:
    mycursor.close()
    mydb.close()