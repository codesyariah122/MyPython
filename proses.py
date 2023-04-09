import os
from db import data_beli_barang


def harga_satuan():
    persentase = input("Masukan persentase yang di inginkan ? ")
    biaya_produksi = input("Masukan biaya produksi ? ")
    screen = ""

    if persentase != "" and biaya_produksi != "":
        for data in data_beli_barang:
            hitung_persentase = round(int(persentase) * 100 / 100)
            nama_barang = data["nama_barang"]
            harga_beli = int(data["harga_beli"])
            harga_satuan = round(harga_beli / int(data["isi"]) - int(biaya_produksi))
            harga_jual = round(harga_satuan + (hitung_persentase * harga_satuan) / 100)
            laba = round(harga_jual - harga_satuan)
            persentase_laba = round((laba / harga_satuan) * 100)

            screen = (
                "Nama Barang : {}".format(nama_barang)
                + "\n"
                + "Persentase : {}".format(hitung_persentase)
                + "\n"
                + "Harga Beli : {}".format(harga_beli)
                + "\n"
                + "Harga Jual : {}".format(harga_jual)
                + " / pcs"
                + "\n"
                + "Laba : {}".format(laba)
                + " / krtn"
                + "\n"
                + "Persentase Laba : {}".format(persentase_laba)
            )

        print(screen)
    else:
        print("Silahkan isi inputan terlebih dahulu !")


def dig_dns():
    domain = input("Masukan nama domain / host yang di inginkan : ").lower()
    input_type = type(domain) == str
    domain_ext = [".com", ".co", ".id"]

    if domain != "":
        if input_type:
            enter_domain = domain.split(".")
            valid_domain = domain_ext.index(".{}".format(enter_domain[1]))
            if valid_domain != "":
                returned_value = os.system("dig {}".format(domain))
                print(returned_value)
        else:
            print("Please input string only !")
    else:
        print("Masukan nama domain ? ")
