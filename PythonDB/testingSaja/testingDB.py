import mysql.connector

host = "localhost"
user = "root"
passwd = "1"

db = mysql.connector.connect(
		host = host,
		user = user,
		passwd = passwd
	)

if db.is_connected():
	print("Berhasil terhubung ke database server")