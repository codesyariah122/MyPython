def tanya():
	nama = input("Siapa nama anda : ?")

	jawaban = nama if nama != "" else "Nama harus di isi"

	print("Hallo, {}".format(jawaban)) 