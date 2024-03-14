import mysql.connector
dataBase = mysql.connector.connect(host="localhost", user="root", passwd="Meraxix@7")


cursorObject = dataBase.cursor()



cursorObject.execute("CREATE DATABASE elderco")
print("ALL DONE!")
