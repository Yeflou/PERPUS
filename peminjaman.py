class Peminjaman:
    def __init__(self, anggota, buku):
        self.anggota = anggota
        self.buku = buku
        self.status = "dipinjam"

    def catat_peminjaman(self):
        print(f"Transaksi: Anggota '{self.anggota.nama}' meminjam buku '{self.buku.judul}'.")

    def catat_pengembalian(self):
        self.status = "dikembalikan"
        print(f"Transaksi: Anggota '{self.anggota.nama}' mengembalikan buku '{self.buku.judul}'.")