import os
nama_tb = 'data_programmer'

def insert_data(db_conn):
	name = input("Nama Lengkap : ")
	email = input("Alamat Email : ")
	phone = input("No Telephone : ")
	if name == "" and email == "" and phone == "":
		print("Input harus diisi ! ")
		show_menu(db_conn)
	else:
		val = (name, email, phone)
		cursor = db_conn.cursor()
		sql = "INSERT INTO {} (name, email, phone) VALUES (%s, %s, %s)".format(nama_tb)
		cursor.execute(sql, val)
		db_conn.commit()

		print("{} data berhasil disimpan".format(cursor.rowcount))

def show_data(db_conn):
	cursor = db_conn.cursor()
	sql = "SELECT * FROM {}".format(nama_tb)
	cursor.execute(sql)
	results = cursor.fetchall()

	if cursor.rowcount < 0:
		print("Belum ada data")
	else:
		print("=========================================================")
		print("+++++++++++++++++++++++ View Data +++++++++++++++++++++++")
		print("=========================================================")

		for data in results:
			print(data)
		print("==========================================================")
		# show_menu(db_conn)

def update_data(db_conn):
	cursor = db_conn.cursor()
	show_data(db_conn)
	id_data = input("pilih id data > - ")
	name = input("New name : ")
	email = input("New email : ")
	phone = input("New phone : ")

	sql = "UPDATE {} SET name=%s, email=%s, phone=%s WHERE id=%s".format(nama_tb)
	val = (name, email, phone, id_data)
	cursor.execute(sql, val)
	db_conn.commit()
	print("{} data berhasil di ubah".format(cursor.rowcount))

def delete_data(db_conn):
	cursor = db_conn.cursor()
	show_data(db_conn)
	id_data = input("Plih id data > - ")
	sql = "DELETE FROM {} WHERE id=%s".format(nama_tb)
	val = (id_data,)
	cursor.execute(sql, val)
	db_conn.commit()
	print("{} data berhasil dihapus".format(cursor.rowcount))
	cursor.execute("ALTER TABLE {} AUTO_INCREMENT=1".format(nama_tb))

def search_data(db_conn):
	cursor = db_conn.cursor()
	keyword = input("Kata unci : ")
	sql = "SELECT * FROM {} WHERE name LIKE %s OR email LIKE %s".format(nama_tb)
	val = ("%{}%".format(keyword), "%{}%".format(keyword))
	cursor.execute(sql, val)
	results = cursor.fetchall()

	if cursor.rowcount < 0:
		print("Data tidak ditemukan ! ")
	else:
		print("Hasil pencarian : ")
		for data in results:
			print(data)


def show_menu(db_conn):
	print("=== OPERATIONAL DATABASE PYTHON ====")
	print("1. Insert Data")
	print("2. Tampilkan Data")
	print("3. Update Data")
	print("4. Delete Data")
	print("5. Search Data")
	print("0 Keluar")
	print("------------------------------------")
	menu = input("Pilih menu> - ")

	# clear screen
	os.system("clear")

	if menu == "1":
		insert_data(db_conn)
	elif menu == "2":
		show_data(db_conn)
	elif menu == "3":
		update_data(db_conn)
	elif menu == "4":
		delete_data(db_conn)
	elif menu == "5":
		search_data(db_conn)
	elif menu == "0":
		exit()
	else:
		print("Maaf menu belum tersedia")

	if __name__ == "__main__":
		while(True):
			show_menu(db_conn)