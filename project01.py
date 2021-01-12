def diffDate(x): #definisikan sebuah function dengan parameter (x)
    import datetime #import modul date and time untuk menggunakan fungsi yang berhubungan dnegan waktu dan tanggal
    tglini = datetime.datetime.now() #tglini berisikan tanggal dan waktu sekarang(now)
    from datetime import datetime #import modul datetime
    tglinput = datetime.strptime(x, "%Y-%m-%d") #konversikan yang ada di parameter x menjadi format datetime
    selisih = tglinput- tglini  #selisih didapat dari tgl yang dimasukkan dengan tanggal ini
    print(abs(selisih.days)) #tampilkan nilai absolut dari selisih (yang diambil harinya saja)

#diffDate("2020-12-31") gak di hidupkan :v nanti kebaca di project 3 