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

sql = "INSERT INTO {} (nama_ular, nama_latin) VALUES (%s, %s)".format(nama_tb)

values = [
		("Mamba Hitam", "Dendroaspis polylepis"),
		("Viper Bertanduk", "Cerastes cerastes")
		]

for val in values:
	cursor.execute(sql, val)
	db.commit()

print("{} data ditambahkan ".format(len(values)))