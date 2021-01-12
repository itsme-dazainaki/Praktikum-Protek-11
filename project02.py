from datetime import * #import semua isi modul datetime 
myfile = open("dataperpus.txt", "w") #buka file text dengan pilihan mode untuk "write"

while True: #perulangan pengisian data menggunakan while
    kode = input("Masukkan Kode Member   : ") #ini untuk inputan kode
    nama = input("Masukkan Nama Member   : ") #ini untuk inputan nama
    judul = input("Masukkan Judul Buku    : ") #ini untuk inputan judul

    pinjam = date.today() #pinjam berisi tanggal hari ini
    kembali = pinjam + timedelta(days = 7) #kembali berisi tanggal pinjam ditambah 7 hari
    data = [kode.upper(), nama, judul, str(pinjam), str(kembali)] #list data brisi kode, nama, tanggal pinjam dan kembali yangg sudah dikonversi ke string
    myfile.write("|".join(data) + "\n") #tambagkan data ke file yang telah dibuka

    print("")
    ulang = input("Ulangi lagi (y/n)      : ") #konfirmasikan pengulangan penginputan data
    print("") 
    if ulang == "y": #jika inputan bernilau y maka
        continue #lanjutkan untuk melakukan perulangan
    if ulang == "n": #jika inputan bernilai n maka
        break #hentikan perulangan

myfile.close() #tutup file untuk mencegah file corrupted atau strukturnya rusak 