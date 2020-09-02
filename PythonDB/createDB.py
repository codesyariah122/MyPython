import mysql.connector

host = 'localhost'
user = 'root'
passwd = '1'

db = mysql.connector.connect(
		host = host,
		user = user,
		passwd = passwd
	)

cursor = db.cursor()
cursor.execute("CREATE DATABASE nama_ular")

print("Database berhasil dibuat")