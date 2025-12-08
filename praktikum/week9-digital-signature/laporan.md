# Laporan Praktikum Kriptografi
Minggu ke-: 9
Topik: Digital Signature (RSA/DSA)  
Nama: Nafis Ramadhan Khoeru Jati 
NIM: 230202769
Kelas: 5IKRB

---

## 1. Tujuan
1. Mengimplementasikan tanda tangan digital menggunakan algoritma RSA.
2. Memverifikasi tanda tangan digital menggunakan public key.
3. Melakukan pengujian integritas pesan melalui percobaan modifikasi pesan.
4. Memahami fungsi tanda tangan digital dalam otentikasi dan integritas data.

---

## 2. Dasar Teori
Tanda tangan digital merupakan mekanisme kriptografi modern yang digunakan untuk menjamin keaslian (authentication) dan integritas (integrity) sebuah pesan. Berbeda dengan enkripsi, tanda tangan digital tidak bertujuan merahasiakan isi pesan, melainkan memastikan bahwa pesan memang dibuat oleh pengirim yang sah dan tidak mengalami perubahan selama proses transmisi.

Pada algoritma RSA, tanda tangan digital dibuat dengan mengenkripsi hash dari pesan menggunakan private key. Sementara itu, verifikasi dilakukan dengan meng-dekripsi tanda tangan menggunakan public key, kemudian mencocokkan hasilnya dengan hash pesan yang diterima. Jika kedua hash sama, tanda tangan dianggap valid.

Jika pesan dimodifikasi sedikit saja, nilai hash akan berubah total sehingga proses verifikasi gagal. Inilah yang membuat tanda tangan digital menjadi alat penting dalam sistem keamanan modern seperti protokol SSL/TLS, software signing, dan dokumen elektronik.

---

## 3. Alat dan Bahan
( - Python 3.11 atau lebih baru
- Library PyCryptodome
- Text editor (VS Code, PyCharm, dsb.)
- Sistem Git & GitHub (untuk commit laporan)
- File program signature.py  )

---

## 4. Langkah Percobaan
1. Menyiapkan struktur folder:
praktikum/week9-digital-signature/
 ├─ src/
 ├─ screenshots/
 └─ laporan.md
2. Menginstall library pendukung:
pip install pycryptodome
3. Membuat file program src/signature.py.
4. Mengimplementasikan:
5. Pembuatan pasangan kunci RSA.
6. Pembuatan tanda tangan digital (digital signature).
7. Verifikasi tanda tangan digital.
8. Percobaan verifikasi gagal ketika pesan diubah.
9. Menjalankan program untuk menghasilkan output dan screenshot.

---

## 5. Source Code
```python
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256

print("=== GENERATE KEY RSA ===")
key = RSA.generate(2048)
private_key = key
public_key = key.publickey()

print("Private Key Length :", len(private_key.export_key()))
print("Public Key Length  :", len(public_key.export_key()))
print()

message = b"Hello, ini pesan penting."
h = SHA256.new(message)

signature = pkcs1_15.new(private_key).sign(h)

print("=== SIGNATURE ===")
print("Message :", message.decode())
print("SHA-256 :", h.hexdigest())
print("Signature (hex):")
print(signature.hex())
print()

print("=== VERIFIKASI PESAN ASLI ===")
try:
    pkcs1_15.new(public_key).verify(h, signature)
    print("Verifikasi berhasil: tanda tangan VALID untuk pesan asli.")
except (ValueError, TypeError):
    print("Verifikasi gagal: tanda tangan TIDAK VALID.")
print()

fake_message = b"Hello, ini pesan palsu."
h_fake = SHA256.new(fake_message)

print("=== VERIFIKASI PESAN PALSU ===")
print("Fake Message :", fake_message.decode())
print("SHA-256 Fake :", h_fake.hexdigest())

try:
    pkcs1_15.new(public_key).verify(h_fake, signature)
    print("Verifikasi berhasil (INI TIDAK BOLEH TERJADI).")
except (ValueError, TypeError):
    print("Verifikasi gagal: tanda tangan TIDAK COCOK dengan pesan palsu.")
print()

print("=== SELESAI ===")
```
---

## 6. Hasil dan Pembahasan
![Hasil Eksekusi](screenshots/output.png)
![Hasil Input](screenshots/input.png)
![Hasil Output](screenshots/output.png)
)

---

## 7. Jawaban Pertanyaan
1. Apa perbedaan utama antara enkripsi RSA dan tanda tangan digital RSA?

Enkripsi RSA bertujuan menjaga kerahasiaan pesan. Pengirim mengenkripsi pesan menggunakan public key, dan hanya penerima yang bisa mendekripsi menggunakan private key.

Tanda tangan digital RSA bertujuan melakukan otentikasi dan integritas. Pengirim membuat tanda tangan menggunakan private key, dan siapa pun dapat memverifikasi menggunakan public key.

Arah penggunaan kunci pada kedua proses tersebut terbalik.

2. Mengapa tanda tangan digital menjamin integritas dan otentikasi pesan?

Karena tanda tangan digital dibuat berdasarkan hash dari pesan. Jika pesan mengalami perubahan sedikit pun, nilai hash akan berbeda, sehingga tanda tangan tidak lagi valid.
Selain itu, hanya pemilik private key yang dapat membuat tanda tangan tersebut, sehingga memastikan identitas pengirim (authentication).

3. Bagaimana peran Certificate Authority (CA) dalam sistem tanda tangan digital modern?

Certificate Authority (CA) berperan sebagai lembaga terpercaya yang menerbitkan dan memverifikasi sertifikat digital yang berisi public key seseorang atau organisasi.
Dengan CA, pengguna lain dapat yakin bahwa public key tersebut benar-benar milik pihak yang sah, sehingga mencegah serangan man-in-the-middle dan pemalsuan identitas.


## 8. Kesimpulan
Dari percobaan ini dapat disimpulkan bahwa tanda tangan digital menggunakan RSA dapat menjamin integritas dan otentikasi pesan. Percobaan menunjukkan bahwa tanda tangan valid hanya untuk pesan asli, sementara pesan yang dimodifikasi menghasilkan verifikasi gagal. Hal ini membuktikan efektivitas mekanisme digital signature sebagai bagian penting dari sistem keamanan informasi modern.

---

## 9. Daftar Pustaka
-

---

## 10. Commit Log
```
week9-digital-signature
Author: Nafis Ramadhan Khoeru Jati <nafisramadhankhoerujati@gmail.com>
Date:   2025-12-8

    week9-digital-signature: implementasi RSA digital signature dan laporan
```



