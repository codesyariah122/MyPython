import pymysql.cursors

connect = pymysql.connect("localhost", "root", "1", "crudajax")

cursor = connect.cursor()

sql = "SELECT * FROM product"

try:
	cursor.execute(sql)

	result = cursor.fetchall()

	for row in result:
		productcode = row[1]
		productname = row[3]
		productprice = row[5]

		print("Product Code = {}, Product Name = {}, Product Price = {}".format(productcode, productname, productprice))
except:
	print("Error : unable to fetch data")

connect.close()