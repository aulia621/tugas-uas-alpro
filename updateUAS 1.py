from prettytable import PrettyTable

databarang = []

def format_currency(value):
    return f"Rp{value:,.2f}"

def input_barang(databarang):
    while True:
        try:
            nama_barang = input("Nama barang: ")
            jumlah_barang = int(input("Jumlah barang: "))
            harga_barang = int(input("Harga barang: "))
            sub = harga_barang * jumlah_barang
            
            # Menambahkan barang yang dimasukkan ke dalam list
            databarang.append({
                "nama barang": nama_barang,
                "jumlah barang": jumlah_barang,
                "harga barang": harga_barang,
                "SubTotal": sub
            })
            print("Barang berhasil dimasukkan")
            
            # Tanyakan apakah ingin melanjutkan atau selesai
            print("-" * 10)
            seleksi = input("Ketik 'selesai' untuk selesai atau 'lanjut' untuk tambah barang lagi: ")
            if seleksi.lower() == 'selesai':
                break
            elif seleksi.lower() != 'lanjut':
                print("Pilihan tidak valid, ketik 'selesai' atau 'lanjut'.")
        except ValueError:
            print("Input tidak valid! Pastikan memasukkan angka yang benar.")

def cetak_transaksi(databarang):
    table_transaksi = PrettyTable(["Nama Barang", "Jumlah Barang", "Harga Barang", "SubTotal"])
    
    total = 0
    for transaksi in databarang:
        total += transaksi["SubTotal"]
        
        table_transaksi.add_row([
            transaksi["nama barang"],
            transaksi["jumlah barang"],
            format_currency(transaksi["harga barang"]),
            format_currency(transaksi["SubTotal"])
        ])

    print(table_transaksi)
    print(f"Total: {format_currency(total)}")
    return total

def pembayaran(subtotal):
    while True:
        try:
            pembayaran = int(input(f"Total yang harus dibayar: Rp {format_currency(subtotal)}\nMasukkan jumlah uang yang dibayar: Rp"))
            if pembayaran < subtotal:
                print("Jumlah pembayaran kurang dari total yang harus dibayar! Silakan masukkan jumlah yang cukup.")
            else:
                kembalian = pembayaran - subtotal
                print(f"Kembalian: Rp {format_currency(kembalian)}")
                return pembayaran, kembalian
        except ValueError:
            print("Input tidak valid! Masukkan angka yang benar.")

def menu(): 
    while True:
        print("-" * 10)
        print("Menu Pilihan")
        print("-" * 10)
        print("1. Tambah barang")
        print("2. Cetak transaksi")
        print("3. Pembayaran")
        print("4. Selesai")
        pilih = input("Pilih menu (1-4): ")
        
        if pilih == "1":
            input_barang(databarang)
        elif pilih == "2":
            cetak_transaksi(databarang)
        elif pilih == "3":
            total = cetak_transaksi(databarang)
            pembayaran_amount, kembalian = pembayaran(total)
            print(f"Total pembayaran: {format_currency(pembayaran_amount)}")
            print(f"Kembalian: {format_currency(kembalian)}")
        elif pilih == "4":
            print("Terima kasih, selesai!")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih sesuai nomor.")

menu()
