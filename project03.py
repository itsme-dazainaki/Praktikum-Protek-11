from datetime import * #import semua isi modul datetime 
import project01 #import modul yang berada di file bernama project01

file = open("dataperpus.txt", "r") #buka file text dengan pilihan mode untuk "write"
baca = file.readlines()  #ini syntax untuk membaca file text yang ada diatas 

kode = input("Masukkan Kode Member     : ") #ini untuk inputan kode
for i in range(len(baca)): #pengecekan kondisi var i dalam range yang ada di "baca"
    if (kode in baca[i]): #jika inputan kode tadi berada di "baca" maka
        isi = baca[i] #isi berisi data yang terdapat pada baca
        isi.replace("\n","") #ganti \n pada isi, menjadi kosong
        data = isi.split("|")  #data bersisi teks dalam isi yang telah dipisah
        print("")
        print("=========== Data Peminjaman Buku ===========")
        print('Kode Member              : ', data[0]) #tampilkan kode member dengan isi dari data indeks ke 0/ data ke 1
        print('Nama Member              : ', data[1]) #tampilkan nama dengan isi dari data indeks ke 1/ data ke 2
        print('Judul Buku               : ', data[2]) #tampilkan judul dengan isi dari data indeks ke 2/ data ke 3
        print('Tanggal Mulai Peminjaman : ', data[3]) #tampilkan tgl pinjam dengan isi dari data indeks ke 3/ data ke 4
        print('Tanggal Maks peminjaman  : ', data[4]) #tampilkan tgl tenggat dengan isi dari data indeks ke 4/ data ke 5
        print('Tanggal Pengembalian     : ', datetime.date(datetime.now())) #tampilkan tanggal sekarang

        t, b, h = (data[4]).split("-") #tahub, bulan, dan hari dihasilkan dari pecahan "data" indeks 4, pisahkan oleh -
        tenggat = date(int(t), int(b), int(h)) #tenggat berisi t,b,h ynag telah di konvert ke format date
        tglkembali = datetime.date(datetime.now()) #tanggal kembali adalah tanggal sekarang
        a = tglkembali - tenggat #lama tgl kembali - tanggal tenggat
        selisih = a.days  #selisih adalah a yang hanya diambil harinya saja
        if selisih <= 0: #jika selisih <= 0 maka 
            selisih = 0 #gaada isinya
            print("Terlambat                :  0 hari") #tampilkan lama terlambat
            print("Denda                    :  Rp 0 ") #tampilkan jumlah denda
        if selisih > 0: #jika selisih > 0 maka
            denda = selisih * 2000 #denda dihasilkan dari selisih *2000
            print("Terlambat                : ", abs(selisih), "hari") #tampilkan lama terlambat
            print("Denda                    :  Rp", denda) #tampilkan jumlah denda
        break #hentikan perulangan
    else : #jika inputan kode tadi tidak berada di "baca" maka
        status = "tidak ada" #statusnya menjadi tidak ada
if status == "tidak ada": #jika nilai status "tidak ada" maka
    print("Maaf !! data yang anda cari tidak ditemukan") #tampilkan yang ada dalam kurung didalam print