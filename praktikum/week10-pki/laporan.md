# Laporan Praktikum Kriptografi
Minggu ke-: 10
Topik: Public Key Infrastructure (PKI) & Certificate Authority 
Nama: Nafis Ramadhan Khoeru Jati
NIM: 230202769
Kelas: 5IKRB

---

## 1. Tujuan
Tujuan dari praktikum ini adalah untuk memahami konsep Public Key Infrastructure (PKI) dan peran Certificate Authority (CA) dalam sistem keamanan jaringan. Mahasiswa diharapkan mampu membuat sertifikat digital sederhana menggunakan Python, memahami proses verifikasi sertifikat, serta menganalisis pentingnya PKI dalam komunikasi aman seperti HTTPS/TLS.

---

## 2. Dasar Teori
Public Key Infrastructure (PKI) adalah sebuah kerangka kerja yang digunakan untuk mengelola kunci publik, sertifikat digital, dan identitas dalam sistem komunikasi yang aman. PKI memanfaatkan kriptografi kunci publik, di mana setiap entitas memiliki pasangan kunci publik dan kunci privat yang digunakan untuk enkripsi, dekripsi, serta penandatanganan digital.

Certificate Authority (CA) merupakan pihak tepercaya yang bertugas menerbitkan dan memverifikasi sertifikat digital. Sertifikat ini berisi informasi identitas pemilik sertifikat beserta kunci publiknya, yang ditandatangani secara digital oleh CA. Dengan adanya CA, pengguna dapat mempercayai bahwa kunci publik benar-benar milik pihak yang sah.

PKI banyak digunakan dalam implementasi protokol keamanan seperti HTTPS dan TLS. Browser web menggunakan PKI untuk memverifikasi keaslian server melalui sertifikat digital, sehingga komunikasi antara klien dan server dapat terlindungi dari penyadapan maupun serangan Man-in-the-Middle (MITM).

---

## 3. Alat dan Bahan
(- Python 3.11
- Visual Studio Code / editor teks lainnya
- Git dan akun GitHub
- Library Python: cryptography

---

## 4. Langkah Percobaan
(Tuliskan langkah yang dilakukan sesuai instruksi.  
Contoh format:
1. Membuat file `caesar_cipher.py` di folder `praktikum/week2-cryptosystem/src/`.
2. Menyalin kode program dari panduan praktikum.
3. Menjalankan program dengan perintah `python caesar_cipher.py`.)

---

## 5. Source Code
(Salin kode program utama yang dibuat atau dimodifikasi.  
Gunakan blok kode:

```python
# contoh potongan kode
def encrypt(text, key):
    return ...
```
)

---

## 6. Hasil dan Pembahasan
(- Lampirkan screenshot hasil eksekusi program (taruh di folder `screenshots/`).  
- Berikan tabel atau ringkasan hasil uji jika diperlukan.  
- Jelaskan apakah hasil sesuai ekspektasi.  
- Bahas error (jika ada) dan solusinya. 

Hasil eksekusi program Caesar Cipher:

![Hasil Eksekusi](screenshots/output.png)
![Hasil Input](screenshots/input.png)
![Hasil Output](screenshots/output.png)
)

---

## 7. Jawaban Pertanyaan
(Jawab pertanyaan diskusi yang diberikan pada modul.  
- Pertanyaan 1: …  
- Pertanyaan 2: …  
)
---

## 8. Kesimpulan
(Tuliskan kesimpulan singkat (2–3 kalimat) berdasarkan percobaan.  )

---

## 9. Daftar Pustaka
(Cantumkan referensi yang digunakan.  
Contoh:  
- Katz, J., & Lindell, Y. *Introduction to Modern Cryptography*.  
- Stallings, W. *Cryptography and Network Security*.  )

---

## 10. Commit Log
(Tuliskan bukti commit Git yang relevan.  
Contoh:
```
commit abc12345
Author: Nama Mahasiswa <email>
Date:   2025-09-20

    week2-cryptosystem: implementasi Caesar Cipher dan laporan )
```
