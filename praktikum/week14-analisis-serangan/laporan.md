# Laporan Praktikum Kriptografi
Minggu ke-: 14  
Topik: Analisis Serangan Kriptografi  
Nama: Nafis Ramadhan Khoeru Jati  
NIM: 230202769  
Kelas: 5IKRB  

---

## 1. Tujuan
Setelah mengikuti praktikum ini, mahasiswa diharapkan mampu:

1. Mengidentifikasi jenis serangan pada sistem informasi nyata.
2. Mengevaluasi kelemahan algoritma kriptografi yang digunakan.
3. Memberikan rekomendasi algoritma kriptografi yang sesuai untuk perbaikan keamanan.

---

## 2. Dasar Teori
Serangan kriptografi merupakan upaya untuk mengeksploitasi kelemahan pada algoritma kriptografi, implementasi sistem, atau konfigurasi keamanan. Salah satu serangan yang umum terjadi adalah brute force dan dictionary attack terhadap password atau hash yang lemah. Algoritma hash seperti MD5 dan SHA-1 sudah tidak direkomendasikan karena memiliki kelemahan collision dan relatif cepat dihitung, sehingga rentan terhadap brute force. Selain itu, kelemahan sering kali tidak hanya berasal dari algoritma, tetapi juga dari implementasi sistem yang tidak menerapkan mekanisme keamanan tambahan seperti salting atau key stretching. Untuk meningkatkan keamanan, sistem modern disarankan menggunakan algoritma yang lebih kuat seperti SHA-256, bcrypt, scrypt, atau Argon2, serta menerapkan konfigurasi keamanan yang tepat.

---

## 3. Alat dan Bahan
(- Python 3.11  
- Visual Studio Code / editor lain  
- Git dan akun GitHub  
- Library tambahan (misalnya pycryptodome, jika diperlukan)  )

---

## 4. Langkah Percobaan
1. Membuat folder `praktikum/week14-analisis-serangan/`.
2. Memilih studi kasus serangan kriptografi pada sistem nyata.
3. Menganalisis jenis serangan dan vektor serangan yang digunakan.
4. Mengevaluasi kelemahan algoritma dan implementasi sistem.
5. Menyusun rekomendasi solusi kriptografi yang lebih aman.
6. Mendokumentasikan hasil analisis dalam file `laporan.md`.

---

## 5. Source Code
Pada praktikum ini tidak dilakukan implementasi program secara langsung, karena fokus kegiatan adalah analisis serangan kriptografi pada sistem nyata. Oleh sebab itu, tidak terdapat source code yang diimplementasikan.

## 6. Hasil dan Pembahasan
Studi kasus yang dianalisis adalah serangan brute force terhadap password yang disimpan menggunakan algoritma hash MD5 tanpa mekanisme salting. Berdasarkan analisis, algoritma MD5 memiliki kecepatan komputasi yang tinggi sehingga memungkinkan penyerang mencoba banyak kombinasi password dalam waktu singkat.

Kelemahan utama pada sistem ini tidak hanya berasal dari algoritma hash yang sudah tidak aman, tetapi juga dari implementasi sistem yang tidak menerapkan mekanisme keamanan tambahan seperti salting dan rate limiting.

Hasil eksekusi program Caesar Cipher:

-

---

## 7. Jawaban Pertanyaan
1. Karena sistem lama masih menggunakan algoritma kriptografi yang sudah usang dan tidak diperbarui sesuai dengan standar keamanan terbaru.
2. Kelemahan algoritma berasal dari desain algoritma itu sendiri, sedangkan kelemahan implementasi berasal dari cara algoritma tersebut diterapkan dalam sistem.
3. Dengan menerapkan algoritma modern, melakukan pembaruan sistem secara berkala, audit keamanan, dan mengikuti standar kriptografi terkini.

---

## 8. Kesimpulan
Berdasarkan praktikum yang dilakukan, dapat disimpulkan bahwa penggunaan algoritma kriptografi yang tidak aman dan implementasi sistem yang lemah dapat menyebabkan sistem rentan terhadap serangan. Pemilihan algoritma yang tepat dan konfigurasi keamanan yang baik sangat penting untuk menjaga keamanan informasi.

---

## 9. Daftar Pustaka
-

---

## 10. Commit Log

```
Author: Nafis Ramadhan Khoeru Jati <nafisramadhankhoerujati@gmail.com>
Date:   2026-01-28

    week14-analisis-serangan-kriptografi
```
