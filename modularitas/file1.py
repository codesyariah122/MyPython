def tanya():
	nama = input("Siapa nama anda : ?")

	jawaban = "Hai, {} ... selamat datang ! ".format(nama) if nama != "" else "Nama harus di isi"

	print(jawaban) 
