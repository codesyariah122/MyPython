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

sql = "DELETE FROM {} WHERE id_ular=%s".format(nama_tb)

val = (3,)

cursor.execute(sql, val)

cnx.commit()

print("{} data dihapus ".format(cursor.rowcount))

cnx.close()