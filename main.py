from buku import Buku
from anggota import Anggota
from petugas import Petugas
from peminjaman import Peminjaman

# Daftar Buku
buku1 = Buku("Pemrograman Python", "Penulis A", "12345")
buku2 = Buku("Struktur Data", "Penulis B", "67890")

# Daftar Anggota
anggota1 = Anggota("Ali", "001")
anggota2 = Anggota("Siti", "002")

# Daftar Petugas
petugas1 = Petugas("Budi", "P001")
petugas2 = Petugas("Dina", "P002")

# Operasi oleh petugas
buku_list = []
petugas1.tambah_buku(buku_list, buku1)
petugas2.tambah_buku(buku_list, buku2)

# Transaksi peminjaman dan pengembalian
peminjaman1 = Peminjaman(anggota1, buku1)
peminjaman1.catat_peminjaman()
anggota1.pinjam_buku(buku1)

print("\n--- Status Buku ---")
print(f"Buku '{buku1.judul}' status: {buku1.status}")

peminjaman2 = Peminjaman(anggota2, buku2)
peminjaman2.catat_peminjaman()
anggota2.pinjam_buku(buku2)

print("\n--- Mengembalikan Buku ---")
peminjaman1.catat_pengembalian()
anggota1.kembalikan_buku(buku1)

print("\n--- Status Akhir Buku ---")
print(f"Buku '{buku1.judul}' status: {buku1.status}")
print(f"Buku '{buku2.judul}' status: {buku2.status}")