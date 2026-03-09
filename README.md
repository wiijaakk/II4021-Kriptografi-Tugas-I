# Tugas 1 II4021 Kriptografi

## Kriptanalisis Sederhana pada Algoritma Kriptografi Klasik dan Steganografi

Repository ini berisi implementasi program dan hasil analisis untuk menyelesaikan **Tugas 1 mata kuliah II4021 Kriptografi**.  Tugas ini berfokus pada pemecahan beberapa tantangan yang menggunakan algoritma kriptografi klasik serta teknik steganografi.

---

## Author

- **Wijaksara Aptaluhung** — 18223088  
- **Gabriela Jennifer Sandy** — 18223092  

Program Studi Sistem dan Teknologi Informasi  
Sekolah Teknik Elektro dan Informatika  
Institut Teknologi Bandung  
2026

---

## Daftar Tantangan

1. **Tantangan Sang Pencuri (Vigenère Cipher)**  
   Kriptanalisis Vigenère Cipher menggunakan metode **Kasiski Examination** dan **analisis frekuensi** untuk menemukan panjang kunci serta melakukan dekripsi ciphertext.

2. **Intersepsi Jaringan (Playfair Cipher)**  
   Dekripsi Playfair Cipher menggunakan **Hill Climbing** dan **quadgram scoring** untuk menemukan matriks kunci yang menghasilkan plaintext bahasa Inggris yang paling masuk akal.

3. **Surat Balasan Sang Pesulap (Affine Cipher)**  
   Kriptanalisis Affine Cipher dengan melakukan **brute force terhadap parameter kunci (a, b)** dan memilih hasil dekripsi yang menghasilkan plaintext yang dapat dipahami.

4. **Laporan yang Terbajak (Hill Cipher)**  
   Pemecahan Hill Cipher menggunakan **Known Plaintext Attack (KPA)** dengan memanfaatkan plaintext yang diketahui untuk merekonstruksi matriks kunci.

5. **Pesan di Balik Cakrawala (Steganografi)**  
   Ekstraksi pesan tersembunyi dari gambar menggunakan teknik **Least Significant Bit (LSB)** pada channel warna tertentu.

6. **Bonus: Ilusi Ekstensi**  
   Analisis tambahan yang menggabungkan teknik **steganografi dan kriptanalisis** untuk menemukan pesan tersembunyi lebih lanjut.

---

## Kesimpulan

Tugas ini menunjukkan bahwa banyak algoritma **kriptografi klasik** dapat dipecahkan dengan kombinasi:

- **Analisis statistik**
- **Algoritma pencarian**
- **Pemrograman**

Pendekatan ini memungkinkan proses kriptanalisis dilakukan secara sistematis untuk menemukan kunci dan plaintext dari ciphertext yang diberikan.
