class Kendaraan(object):

	def __init__(self, nama):
		self.nama = nama
		self.penumpang = []

	def tambah_penumpang(self, nama_penumpang):
		self.penumpang.append(nama_penumpang)

class Motor(Kendaraan):

	def tambah_penumpang(self, nama_penumpang):
		if len(self.penumpang) < 2:
			super(Motor, self).tambah_penumpang(nama_penumpang)
		else:
			print("Maaf {}, anda tidak bisa masuk".format(nama_penumpang))


motor = Motor("Motorku")
motor.tambah_penumpang("Iim Marlina")
motor.tambah_penumpang("Jennymar")

print("Penumpang : "+str(motor.penumpang))