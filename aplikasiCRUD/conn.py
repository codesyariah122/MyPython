import mysql.connector
import os

host = 'localhost'
user = 'root'
passwd = '1'
nama_db = 'adv_data'

cnx = mysql.connector.connect(
		host = host,
		user = user,
		password = passwd,
		database = nama_db
	)
if cnx.is_connected():
	print("Berhasil terhubung ke server")

	# cnx.close()


# curDir = os.getcwd()
# print(curDir)