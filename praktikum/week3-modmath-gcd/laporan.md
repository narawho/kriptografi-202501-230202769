# Laporan Praktikum Kriptografi
Minggu ke-: 3
Topik: Aritmetika Modular, GCD, Bilangan Prima, Logaritma Diskrit  
Nama: Nafis Ramadhan Khoeru Jati
NIM: 230202769
Kelas: 5IKRB  

---

## 1. Tujuan
Setelah mengikuti praktikum ini, mahasiswa diharapkan mampu:

1. Menyelesaikan operasi aritmetika modular.
2. Menentukan bilangan prima dan menghitung GCD (Greatest Common Divisor).
3. Menerapkan logaritma diskrit sederhana dalam simulasi kriptografi.

---

## 2. Dasar Teori
Modular arithmetic adalah sistem perhitungan yang bekerja berdasarkan sisa hasil bagi suatu bilangan terhadap bilangan modulus tertentu. Dua bilangan dikatakan kongruen jika memiliki sisa pembagian yang sama terhadap modulus yang digunakan, ditulis sebagai 
𝑎≡𝑏 (mod 𝑛) a≡b (modn). Konsep ini banyak digunakan dalam kriptografi karena memungkinkan operasi pada bilangan besar tetap efisien dan aman, serta menjadi dasar dari algoritma seperti RSA dan Diffie-Hellman.
Greatest Common Divisor (GCD) atau Faktor Persekutuan Terbesar adalah bilangan terbesar yang dapat membagi dua bilangan tanpa sisa. Perhitungannya umumnya dilakukan dengan Algoritma Euclidean yang cepat dan sederhana. Dalam kriptografi, GCD digunakan untuk memastikan dua bilangan bersifat relatif prima, sehingga memungkinkan perhitungan invers modular yang penting dalam pembentukan kunci publik dan privat pada sistem seperti RSA.

---

## 3. Alat dan Bahan
( - Python 3.12.2
- Visual Studio Code / editor lain  
- Git dan akun GitHub  
)

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
