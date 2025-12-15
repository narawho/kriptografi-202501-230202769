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
- Python 3.11
- Visual Studio Code / editor teks lainnya
- Git dan akun GitHub
- Library Python: cryptography

---

## 4. Langkah Percobaan
1. Membuat struktur folder praktikum/week10-pki/ yang terdiri dari folder src, screenshots, dan file laporan.md.
2. Menginstal library Python yang diperlukan menggunakan perintah pip install cryptography.
3. Membuat file pki_cert.py di dalam folder src/.
4. Menuliskan kode program Python untuk menghasilkan pasangan kunci RSA dan sertifikat digital self-signed.
5. Menjalankan program menggunakan perintah python pki_cert.py.
6. Mengamati hasil berupa file sertifikat digital dengan format .pem.
7. Mengambil screenshot hasil eksekusi program sebagai bukti praktikum.
   
---

## 5. Source Code

```python
from cryptography import x509
from cryptography.x509.oid import NameOID
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from datetime import datetime, timedelta

key = rsa.generate_private_key(
public_exponent=65537,
key_size=2048
)

subject = issuer = x509.Name([
x509.NameAttribute(NameOID.COUNTRY_NAME, u"ID"),
x509.NameAttribute(NameOID.ORGANIZATION_NAME, u"UPB Kriptografi"),
x509.NameAttribute(NameOID.COMMON_NAME, u"example.com"),
])

cert = (
x509.CertificateBuilder()
.subject_name(subject)
.issuer_name(issuer)
.public_key(key.public_key())
.serial_number(x509.random_serial_number())
.not_valid_before(datetime.utcnow())
.not_valid_after(datetime.utcnow() + timedelta(days=365))
.sign(key, hashes.SHA256())
)

with open("cert.pem", "wb") as f:
    f.write(cert.public_bytes(serialization.Encoding.PEM))


print("Sertifikat digital berhasil dibuat: cert.pem")
```
)

---

## 6. Hasil dan Pembahasan

![Hasil Eksekusi](screenshot/hasil.png)
)

---

## 7. Jawaban Pertanyaan
1. Apa fungsi utama Certificate Authority (CA)?
Fungsi utama CA adalah menerbitkan, memverifikasi, dan menandatangani sertifikat digital untuk memastikan keaslian identitas pemilik kunci publik.

2. Mengapa self-signed certificate tidak cukup untuk sistem produksi?
Karena self-signed certificate tidak divalidasi oleh pihak tepercaya, sehingga browser atau klien tidak dapat memastikan keaslian server dan berpotensi menimbulkan risiko keamanan.

3. Bagaimana PKI mencegah serangan MITM dalam komunikasi TLS/HTTPS?
PKI mencegah serangan MITM dengan memastikan bahwa sertifikat server telah diverifikasi oleh CA tepercaya, sehingga klien dapat yakin bahwa mereka berkomunikasi dengan server yang sah.

---

## 8. Kesimpulan
Berdasarkan praktikum yang dilakukan, dapat disimpulkan bahwa PKI memiliki peran penting dalam menjaga keamanan komunikasi digital. Sertifikat digital dan CA memungkinkan proses verifikasi identitas secara tepercaya. Praktikum ini berhasil menunjukkan proses pembuatan sertifikat digital sederhana menggunakan Python.

---

## 9. Daftar Pustaka

---

## 10. Commit Log
```
commit abc12345
Author: Nama Mahasiswa <email>
Date:   2025-09-20

    week2-cryptosystem: implementasi Caesar Cipher dan laporan )
```
