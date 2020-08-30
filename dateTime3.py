# from datetime import datetime
# sekarang = datetime.now()

# tahun = sekarang.year

# bulan = sekarang.month

# hari = sekarang.day


# print("Sekarang : {0}/{1}/{2} ".format(hari, bulan, tahun))

from datetime import datetime

kini = datetime.now()

jam = kini.hour
menit = kini.minute
detik = kini.second

print("Sekarang : {0}:{1}:{2} ".format(jam, menit, detik))