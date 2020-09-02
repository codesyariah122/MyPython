import mysql.connector

host = 'localhost'
user = 'root'
passwd = '1'
nama_db = 'nama_ular'

cnx = mysql.connector.connect(
		host = host,
		user = user,
		password = passwd
	)

cursor = cnx.cursor()
cursor.execute("CREATE DATABASE {}".format(nama_db))

print("Database berhasil dibuat")