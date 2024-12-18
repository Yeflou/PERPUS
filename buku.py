class Buku:
    def __init__(self, judul, penulis, ISBN, status="tersedia"):
        self.judul = judul
        self.penulis = penulis
        self.ISBN = ISBN
        self.status = status

    def pinjam_buku(self):
        if self.status == "tersedia":
            self.status = "dipinjam"
            print(f"Buku '{self.judul}' berhasil dipinjam.")
        else:
            print(f"Buku '{self.judul}' sedang tidak tersedia.")

    def kembalikan_buku(self):
        if self.status == "dipinjam":
            self.status = "tersedia"
            print(f"Buku '{self.judul}' berhasil dikembalikan.")
        else:
            print(f"Buku '{self.judul}' sudah tersedia.")
            
print("Ayangnya Avi cuma Flora")