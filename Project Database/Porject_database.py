import mysql.connector
import uuid
db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database= '5220411238'
    )
cursor = db.cursor(dictionary=True)
class Penjual:
        
    def tambah_produk(self,nama,harga,stok):
        query = "INSERT INTO produk(nama,harga,stok) VALUES(%s,%s,%s)"
        value = (nama,harga,stok,)
        cursor.execute(query,value)
        db.commit()
        print("Produk berhasil ditambahkan")
        
    def display_produk(self,one=None):
        cursor.execute("SELECT * FROM produk")
        hasil = cursor.fetchall()
        print("------------------------------------")
        print("| id |     nama    |  harga | stok |")
        print("------------------------------------")
        if one is None:
            for row in hasil:
                print(f"| {row['id']:<3}| {row['nama']:<11} | {row['harga']:<6} |  {row['stok']:<4}|")
        else:
            print(f"| {one['id']:<3}| {one['nama']:<11} | {one['harga']:<6} |  {one['stok']:<4}|")
        print("------------------------------------")
        return hasil
    
    def __update_stok_produk(self,id):
        cursor.execute(f"SELECT * FROM produk WHERE id={id}")
        hasil = cursor.fetchone()
        self.display_produk(hasil)
        stok = int(input("Masukan Stok Baru = "))
        cursor.execute(f"UPDATE produk SET stok={stok} WHERE id={id} ")
        db.commit()
        print("---Sukses Mengupdate Stok!---")
        
    def __delete_produk(self,id):
        cursor.execute(f"DELETE FROM produk WHERE id={id}")
        db.commit()
        print("---Produk Sukses Dihapus!---")
        
    def dashboard_penjual(self):
        while True:
            print("=====Dashboard Penjual=====")
            print("1. Tambah Produk")
            print("2. Tampilkan Produk")
            print("3. Update Stok Produk")
            print("4. Delete Produk")
            print("0. Exit")
            
            choose = int(input("Masukan Pilihan Anda : "))
            
            if choose == 1:
                nama = input("Masukan Nama Produk : ")
                harga = int(input("Masukan Harga Produk : "))
                stok = int(input("Masukan Stok : "))
                self.tambah_produk(nama,harga,stok)
            elif choose == 2:
                self.display_produk()
            elif choose == 3:
                self.display_produk()
                id = int(input('Masukan Id produk : '))
                self._Penjual__update_stok_produk(id)
            elif choose == 4:
                self.display_produk()
                id = int(input('Masukan Id produk : '))
                self._Penjual__delete_produk(id)
            else:
                break
class Pembeli(Penjual):
    
    def buat_transaksi(self,id,customer,jumlah):
        new_uuid = uuid.uuid4()
        id_transaksi = str(new_uuid)[:8]
        cursor.execute(f"SELECT * FROM produk WHERE id={id}")
        hasil = cursor.fetchone()
        total = hasil['harga'] * jumlah
        query = "INSERT INTO transaksi(id_transaksi,nama_pembeli,nama_barang,jumlah,total) VALUES(%s,%s,%s,%s,%s)"
        value = (id_transaksi,customer,hasil['nama'],jumlah,total)
        cursor.execute(query,value)
        db.commit()
        stok = hasil['stok'] - jumlah
        cursor.execute(f"UPDATE produk SET stok={stok} WHERE id={id}")
        db.commit()
        return id_transaksi
        
    
    def invoice(self,id_transaksi):
        cursor.execute(f"SELECT * FROM transaksi WHERE id_transaksi=%s",(id_transaksi,))
        hasil = cursor.fetchone()
        print("----Invoice----")
        print("Id Transaksi : ",hasil['id_transaksi'])
        print("Nama Pembeli : ",hasil['nama_pembeli'])
        print("Nama Barang : ",hasil['nama_barang'])
        print("Jumlah : ",hasil['jumlah'])
        print("Total Harga : ",hasil['total'])
        print("---------------")
        
    def dashboard_pembeli(self):
        while True:
            super().display_produk()
            id = int(input("Pilih Id Produk :"))
            nama = input("Masukan Nama Anda : ")
            jumlah = int(input("Jumlah : "))
            id_trx = self.buat_transaksi(id,nama,jumlah)
            pembeli.invoice(id_trx)
            choice = input("Apakah ingin beli lagi? y/n : ")
            if choice.lower() != 'y':
                break
penjual = Penjual()
pembeli = Pembeli()
while True:
    print("1. Penjual")
    print("2. Pembeli")
    print("0. exit")
    choose = int(input("Anda Sebagai Siapa? 1/2/0 : "))
    if choose == 1:
        penjual.dashboard_penjual()
    elif choose == 2:
        pembeli.dashboard_pembeli()
    else:
        break
