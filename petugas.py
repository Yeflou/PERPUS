class Petugas:
    def __init__(self, nama, id_petugas):
        self.nama = nama
        self.id_petugas = id_petugas

    def tambah_buku(self, buku_list, buku):
        buku_list.append(buku)
        print(f"Petugas '{self.nama}' menambahkan buku '{buku.judul}'.")

    def hapus_buku(self, buku_list, buku):
        if buku in buku_list:
            buku_list.remove(buku)
            print(f"Petugas '{self.nama}' menghapus buku '{buku.judul}'.")
        else:
            print(f"Buku '{buku.judul}' tidak ditemukan.")