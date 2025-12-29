# Laporan Praktikum Kriptografi
Minggu ke-: 11
Topik: Shamir’s Secret Sharing (SSS)
Nama: Nafis Ramadhan Khoeru Jati
NIM: 230202769
Kelas: 5IKRB

---

## 1. Tujuan
Setelah mengikuti praktikum ini, mahasiswa diharapkan mampu:
1. Menjelaskan konsep Shamir Secret Sharing (SSS).
2. Melakukan simulasi pembagian rahasia ke beberapa pihak menggunakan skema SSS.
3. Menganalisis keamanan skema distribusi rahasia.

---

## 2. Dasar Teori
Shamir's Secret Sharing (SSS) adalah algoritma kriptografi yang memungkinkan sebuah rahasia dibagi menjadi beberapa bagian yang disebut shares. Algoritma ini menggunakan konsep ambang batas atau threshold (k, n), di mana sebuah rahasia dibagi menjadi $n$ bagian, namun hanya membutuhkan minimal $k$ bagian untuk dapat merekonstruksi rahasia tersebut secara utuh.Secara matematis, SSS bekerja berdasarkan prinsip Interpolasi Lagrange dan polinomial di atas medan hingga (modular arithmetic). Rahasia diletakkan sebagai konstanta $a_0$ dalam polinomial berderajat $k-1$. Tanpa jumlah share yang memenuhi ambang batas $k$, penyerang tidak akan mendapatkan informasi apa pun mengenai rahasia asli, menjadikannya skema yang memiliki tingkat keamanan teoretis yang tinggi.

---

## 3. Alat dan Bahan
(- Python 3.11 atau lebih baru
- Visual Studio Code / editor lain
- Library secretsharing
- Git dan akun GitHub  )

---

## 4. Langkah Percobaan
1. Membuat struktur folder praktikum/week11-secret-sharing/src/ dan screenshots/.
2. Menginstal library yang dibutuhkan dengan perintah pip install secretsharing.
3. Membuat file secret_sharing.py di dalam folder src/.
4. Mengimplementasikan kode program untuk membagi rahasia (split) menjadi 5 bagian dengan threshold 3.
5. Mengimplementasikan kode program untuk merekonstruksi (recover) rahasia dari subset share yang ada.
6. Menjalankan program dan mendokumentasikan hasilnya.

---

## 5. Source Code
(Salin kode program utama yang dibuat atau dimodifikasi.  
Gunakan blok kode:

```python
from secretsharing import SecretSharer

secret = "KRIPUPB2025"

secret_hex = secret.encode().hex()

shares = SecretSharer.split_secret(secret_hex, 3, 5)
print("Shares:", shares)

recovered_hex = SecretSharer.recover_secret(shares[:3])
recovered = bytes.fromhex(recovered_hex).decode()

print("Recovered secret:", recovered)

```
)

---

## 6. Hasil dan Pembahasan
![Hasil Eksekusi](screenshot/hasil.png)

---

## 7. Jawaban Pertanyaan
1. Keuntungan SSS dibanding salinan langsung: SSS menghilangkan single point of failure. Jika salinan kunci langsung dicuri, rahasia terbongkar. Di SSS, pencuri harus mendapatkan minimal $k$ bagian. Selain itu, jika satu orang kehilangan kuncinya, rahasia masih bisa dipulihkan selama jumlah pemegang kunci lainnya memenuhi threshold.
2. Peran Threshold (k): Menentukan titik keseimbangan antara keamanan dan ketersediaan. Semakin tinggi $k$, semakin sulit bagi penyerang untuk berkolusi mencuri rahasia, namun semakin tinggi pula risiko rahasia tidak bisa dibuka jika banyak orang kehilangan share-nya.
3. Contoh Skenario Nyata: Manajemen kunci pada cryptocurrency wallet (Multisig), di mana transaksi hanya sah jika disetujui oleh sejumlah pihak tertentu dari total pemilik otoritas.
---

## 8. Kesimpulan
Percobaan ini menunjukkan bahwa Shamir’s Secret Sharing sangat efektif untuk mendistribusikan kepercayaan (trust) tanpa memberikan rahasia sepenuhnya kepada satu pihak. Melalui penggunaan polinomial, rahasia dapat direkonstruksi dengan aman hanya jika ambang batas (threshold) terpenuhi.

---

## 9. Daftar Pustaka
-

---

## 10. Commit Log
(
```
commit week 11 -secret sharing
Author: Nafis Ramadhan Khoeru Jati <nafisramadhankhoerujati@gmail.com>
Date:   2025-12-29

    week11-cryptosystem: secret sharing )
```
