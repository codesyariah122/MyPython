import mysql.connector

host = 'localhost'
user = 'root'
passwd = '1'
db = 'nama_ular'

cnx = mysql.connector.connect(
		host = host,
		user = user,
		password = passwd
	)

if cnx.is_connected():
	print("Berhasil terhubung ke server")

cnx.close()