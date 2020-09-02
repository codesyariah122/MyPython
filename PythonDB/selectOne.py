import mysql.connector

host = 'localhost'
user = 'root'
passwd = '1'
nama_db = 'nama_ular'
nama_tb = 'ular_berbisa'

cnx = mysql.connector.connect(
		host = host,
		user = user,
		password = passwd,
		database = nama_db
	)

cursor = cnx.cursor()

sql = "SELECT * FROM {}".format(nama_tb)

cursor.execute(sql)

results = cursor.fetchone()

print(results)

# for data in results:
# 	print(data)

cnx.close()