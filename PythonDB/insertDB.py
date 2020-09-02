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

val = ("King Cobra", "Ophiophagus hannah")

cursor.execute(sql, val)


db.commit()

print("{} data ditambahkan ".format(cursor.rowcount))