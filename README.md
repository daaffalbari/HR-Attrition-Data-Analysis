# Proyek Akhir: Menyelesaikan Permsalahan HR Perusahaan Jaya Jaya Maju

## Business Understanding

Jaya Jaya Maju merupakan salah satu perusahaan multinasional yang telah berdiri sejak tahun 2000. Ia memiliki lebih dari 1000 karyawan yang tersebar di seluruh penjuru negeri. Walaupun telah menjadi menjadi perusahaan yang cukup besar, Jaya Jaya Maju masih cukup kesulitan dalam mengelola karyawan. Hal ini berimbas tingginya attrition rate (rasio jumlah karyawan yang keluar dengan total karyawan keseluruhan) hingga lebih dari 10%.

### Permasalahan Bisnis

1. Tingginya attrition rate
2. Keterbatasan monitoring pegawai

### Cakupan Proyek

Proyek ini mencakup serangkaian proses pengolahan data, dimulai dari tahap penilaian (assessing) hingga tahap pembersihan (cleaning) data, terutama jika ditemukan duplikasi atau nilai yang hilang (missing value). Selanjutnya, dilakukan analisis eksplorasi data (exploratory data analysis) guna memahami pola dan karakteristik data. Tahapan berikutnya meliputi pengembangan model machine learning yang bertujuan untuk membangun model prediksi. Selain itu, proyek ini juga mencakup pembuatan dashboard bisnis yang berfungsi sebagai alat pemantauan perkembangan proyek secara keseluruhan.

Adapun output yang diharapkan dari proyek ini meliputi:

1. Visualisasi data dari exploratory data analysis — Menyajikan ringkasan data secara visual agar pola dan perilaku data lebih mudah dipahami.
2. Tabel statistik korelasi — Mengidentifikasi faktor-faktor yang memiliki pengaruh signifikan terhadap tingkat attrition.
3. Model machine learning — Merancang dan menentukan model machine learning yang paling sesuai dengan kebutuhan proyek.
4. Evaluasi model — Mengevaluasi performa model yang telah dibuat guna memastikan keakuratannya.
5. Model prediksi — Mengembangkan model prediktif untuk mengidentifikasi kemungkinan terjadinya attrition.
6. Dashboard bisnis — Membuat dashboard interaktif yang memungkinkan pemantauan kinerja dan perkembangan proyek secara real-time.

### Persiapan

1. Sumber data: https://github.com/dicodingacademy/dicoding_dataset/tree/main/employee

OR

2. Using Supabase:

Setup Environment Variables:

```
- user=postgres.ssutselshxgtnmodszvg
- password=dicoding123
- host=aws-0-ap-southeast-1.pooler.supabase.com
- port=6543
- dbname=postgres
```

```bash
postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}:{PORT}/{DBNAME}?sslmode=require
```

2. Setup Environment
   **Open CMD or Terminal, to install all requirements, run:**

```bash
pip install -r requirements.txt
```

**Login to Metabase**

Email: daffaa.albari@gmail.com
Password: dicoding123

## Business Dashboard

Dashboard ini dirancang untuk memantau masalah attrition di perusahaan. Berikut adalah penjelasan mengenai isinya:

1. **Jumlah Karyawan dan Attrition**:

Dashboard ini menampilkan total jumlah karyawan sebanyak 1,058 orang, dengan visualisasi distribusi attrition. Rasio karyawan yang meninggalkan perusahaan menjadi perhatian penting.

2. **Attrition Berdasarkan Departemen**:

Analisis menunjukkan bahwa departemen dengan jumlah attrition tertinggi adalah Sales dan Research & Development. Ini bisa menjadi indikator bahwa faktor lingkungan kerja atau tanggung jawab di departemen ini membutuhkan perhatian lebih.

3. **Jarak Tempat Tinggal dari Kantor**:

Grafik menunjukkan bagaimana jarak tempat tinggal memengaruhi tingkat attrition. Karyawan yang tinggal lebih dekat dengan kantor cenderung memiliki tingkat attrition yang lebih rendah.

4. **Attrition Berdasarkan Job Role**:

Berdasarkan job role, grafik mendeteksi bahwa Sales Executive dan Research Scientist memiliki jumlah karyawan tertinggi. Pengamatan ini bisa dikaitkan dengan faktor-faktor spesifik di bidang pekerjaan tersebut yang memengaruhi keputusan mereka untuk tetap atau meninggalkan perusahaan.

5. **Faktor Keuangan**:

Analisis menunjukkan bahwa ada hubungan antara kenaikan gaji dan tingkat attrition. Semakin rendah kenaikan gaji, semakin tinggi kemungkinan karyawan meninggalkan perusahaan.

6. **Pengaruh Kerja Terhadap Attrition**:

Faktor lembur dan keseimbangan kerja-kehidupan memiliki dampak signifikan terhadap attrition. Karyawan yang sering lembur dan memiliki keseimbangan kehidupan kerja yang buruk lebih cenderung meninggalkan perusahaan.

7. **Keseimbangan Kerja dan Kehidupan**:
   Karyawan dengan tingkat kepuasan kerja yang baik cenderung tidak meninggalkan perusahaan. Perusahaan perlu memastikan lingkungan kerja yang mendukung dan kondusif untuk menurunkan tingkat attrition.

Dashboard ini membantu perusahaan mengidentifikasi dan mengambil tindakan terhadap faktor-faktor yang berkontribusi pada tingkat attrition, seperti kompensasi, lingkungan kerja, dan keseimbangan kerja-kehidupan.

## Conclusion

Dari pembuatan dashboard yang telah dilakukan, didapatkan kesimpulan bahwa Attrition rate paling banyak berada pada **Departemen HR** dengan job role **Laboratory Technician & Research Scientist** dan pada **Departemen Sales** dengan job role **Sales Excecutive & Sales Representative**.
Banyak juga karyawan yang keluar dari latar belakang pendidikan teknik dan marketing. Hal yang diperhatikan juga kebijakan lembur/over time yang diberikan kepada karyawan yang berpengaruh pada attrition rate.

## Recomendation Action Items

1. Mengevaluasi lingkungan pekerjaan pada departemen atau job role yang memiliki tingkat attration yang tinggi guna meningkatkan kepuasan pegawai
2. Mengurangi beban kerja pegawai seperti melakukan penambahan pegawai untuk mengakomodir jumlah pekerjaan yang banyak
3. Memberikan lebih banyak kesempatan pelatihan bagi pegawai agar pegawai dapat berkembang
4. Memberikan gaji dan kenaikan gaji yang sesuai agar pegawai merasa lebih dihargai dan lebih termotivasi
5. Evaluasi dampak jam kerja tambahan (overtime) terhadap tingkat attrition. Pertimbangkan kebijakan yang lebih baik untuk mengelola beban kerja dan mendorong keseimbangan kehidupan kerja yang lebih baik.

## Guides to run project dan melakukan prediksi

Open CMD or PowerShell, to install all requirements, run:

```bash
cd <name_folder>
pip install -r requirements.txt
python prediction.py
```
