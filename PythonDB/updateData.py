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

sql = "UPDATE {} SET nama_ular=%s, nama_latin=%s WHERE id_ular=%s".format(nama_tb)
val = ("Mamba Hijau", "Dendroaspis angusticeps", 3)
cursor.execute(sql, val)

cnx.commit()

print("{} data diupdate".format(cursor.rowcount))

cnx.close()