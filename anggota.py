class Anggota:
    def __init__(self, nama, id_anggota):
        self.nama = nama
        self.id_anggota = id_anggota
        self.riwayat_peminjaman = []

    def pinjam_buku(self, buku):
        buku.pinjam_buku()
        if buku.status == "dipinjam":
            self.riwayat_peminjaman.append(buku.judul)

    def kembalikan_buku(self, buku):
        buku.kembalikan_buku()