import mysql.connector

host = 'localhost'
user = 'root'
passwd = '1'
db = 'nama_ular'
nama_tb = 'ular_berbisa'

db = mysql.connector.connect(
		host = host,
		user = user,
		passwd = passwd,
		database = db
	)

cursor = db.cursor()

sql = """CREATE TABLE {} (
	id_ular INT AUTO_INCREMENT PRIMARY KEY,
	nama_ular VARCHAR(255),
	nama_latin VARCHAR(255)
)
"""

cursor.execute(sql.format(nama_tb))

print("Table ular_berbisa berhasil dibuat")