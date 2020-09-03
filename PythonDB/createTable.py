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

sql = """CREATE TABLE {} (
	id_ular INT AUTO_INCREMENT PRIMARY KEY,
	nama_ular VARCHAR(255),
	nama_latin VARCHAR(255)
)
"""

cursor.execute(sql.format(nama_tb))

print("Table ular_berbisa berhasil dibuat")