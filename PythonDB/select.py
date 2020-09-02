import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="1",
  database="nama_ular"
)

cursor = db.cursor()
sql = "SELECT * FROM ular_berbisa"
cursor.execute(sql)

results = cursor.fetchall()

for data in results:
  print(data)