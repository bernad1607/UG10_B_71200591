daftar=input("masukan daftar siswa").title().split(",")
print("daftar siswa :,daftar")

tambah=input("daftar siswa yang ingin ditambahkan : ").lower()
if tambah.title() in daftar:
    print("daftar siswa" +tambah.upper()+ "daftar tambahan yang sudah ada")
else:
    daftar.append("tambah".upper())
    print("jumlah penambahan siswa pada daftar"+"daftar")

    