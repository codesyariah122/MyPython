import pymysql.cursors

db = pymysql.connect("localhost", "root", "1", "crudajax")
cursor = db.cursor()

cursor.execute("SELECT VERSION()")

data = cursor.fetchone()

print("Database version : %s " % data)

db.close()