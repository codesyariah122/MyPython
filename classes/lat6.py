class Kendaraan(object):
	penumpang = []

	def __init__(self, nama):
		self.nama = nama
		self.penumpang = []

	def tambah_penumpang(self, nama_penumpang):
		self.penumpang.append(nama_penumpang)

# code di bawah ini untuk menginstansiasi class
mobil = Kendaraan("Mobil")
motor = Kendaraan("Motor")

mobil.tambah_penumpang("Michaele Schumacher")
mobil.tambah_penumpang("Rio Haryanto")

motor.tambah_penumpang("Nico Rosberg")

print(motor.penumpang)
print(mobil.penumpang)