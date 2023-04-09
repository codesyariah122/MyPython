from data_barang import data_beli_barang

def hitung_laba():
    percentased = input("Masukan persentase yang di inginkan : ")
    biaya_produksi = input("Masukan biaya produksi : ")
    screen = ""
    if percentased != "" and biaya_produksi != "":
        for data in data_beli_barang:
            percentase = round((int(percentased) * 100) / 100)
            nama_barang = data["nama_barang"].lower()
            harga_beli = int(data["harga_beli"])
            harga_satuan = round(harga_beli / int(data["isi"])) + int(biaya_produksi)
            harga_jual = round(harga_satuan + (percentase * harga_satuan) / 100)
            laba = round(harga_jual - harga_satuan)
            persentase_laba = round((laba / harga_satuan) * 100)
            screen = (
                "Nama Barang : {}".format(nama_barang)
                + "\n"
                + "Persentase : {}".format(percentase)
                + "\n"
                + "Harga Beli : {}".format(harga_beli)
                + "\n"
                + "Harga Jual : {}".format(harga_jual)
                + " / pcs"
                + "\n"
                + "Laba Kotor : {}".format(laba)
                + " / krtn"
                + "\n"
                + "Persentase Laba : {}".format(persentase_laba)
            )

        print(screen)
    else:
        print("Silahkan isi input terlebih dahulu !")
