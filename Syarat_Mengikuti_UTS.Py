nama = str(input("masukkan nama : "))
kehadiran = int(input("masukkan jumlah kehadiran : "))
bayar = str(input("bayar tagihan(sudah / belum ) : "))
cetak_kartu = str(input("cetak kartu(sudah ? belum ) : "))

if(nama and kehadiran >= 7 and bayar =="sudah" and cetak_kartu =="sudah"):
    print(f'Nama {nama} dengan jumlah kehadiran : {kehadiran} kali')
    print(f'Membayar Tagihan ({bayar}) dan Cetak Kartu : ({cetak_kartu})')
    print("Selamat kamu bisa mengikuti ujian")
else:
    print("Kamu tidak bisa mengikuti ujian")
    print(f'Nama {nama} dengan jumlah kehadiran : {kehadiran} kali')
    print(f'Membayar Tagihan ({bayar}) dan Cetak Kartu : {cetak_kartu}')
