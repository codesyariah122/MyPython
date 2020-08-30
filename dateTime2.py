from datetime import datetime

sekarang = datetime.now()

tahun = sekarang.year

bulan = sekarang.month

hari = sekarang.day

print("sekarang : {2}-{1}-{0}".format(tahun, bulan, hari))