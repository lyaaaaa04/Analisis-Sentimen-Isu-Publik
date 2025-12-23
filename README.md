# Analisis Sentimen Isu Publik terkait Penutupan TPA Suwung

## Deskripsi Proyek
Proyek ini merupakan salah satu bentuk **luaran Praktik Kerja Lapangan (PKL)** yang dikerjakan di **Dinas Komunikasi, Informatika, dan Statistik Kota Denpasar**. Proyek ini bertujuan untuk melakukan **analisis sentimen masyarakat terhadap isu penutupan TPA Suwung**, yang merupakan tempat pembuangan akhir terbesar di Provinsi Bali.

Sistem dikembangkan menggunakan pendekatan **machine learning** dengan menerapkan empat algoritma klasifikasi, yaitu **Support Vector Machine (SVM)**, **Multinomial Naive Bayes**, **XGBoost**, dan **Logistic Regression**.

Fokus utama proyek ini tidak hanya pada pencapaian akurasi model, tetapi juga pada **insight yang diperoleh dari hasil analisis sentimen**, khususnya untuk mengetahui apakah **Kota Denpasar terdampak secara signifikan** oleh isu penutupan TPA Suwung berdasarkan persepsi masyarakat di media sosial.

---

## Dataset
- Dataset dikumpulkan melalui proses **crawling komentar Instagram** terkait isu penutupan TPA Suwung.
- Jumlah data: **733 komentar**
- Jumlah kelas sentimen: **2 kelas**
  - Positif
  - Negatif

---

## Alur Implementasi
Tahapan utama dalam proyek ini meliputi:

1. Load dataset teks
2. Pra-pemrosesan data teks
3. Ekstraksi fitur menggunakan **TF-IDF**
4. Penyeimbangan data menggunakan **SMOTE**
5. Pembagian data menjadi data training dan testing
6. Training model menggunakan algoritma SVM, Multinomial Naive Bayes, XGBoost, dan Logistic Regression
7. Evaluasi performa model
8. Visualisasi hasil analisis menggunakan **wordcloud**
9. Penyimpanan model terbaik

---

## Pra-pemrosesan Teks
Tahapan pra-pemrosesan teks yang diterapkan pada dataset meliputi:
- Pembersihan data (penghapusan URL, simbol, emoji, dan karakter tidak relevan)
- Case folding (konversi huruf menjadi huruf kecil)
- Normalisasi kata slang
- Stopword removal
- Tokenisasi kata
- Stemming

---

## Penanganan Ketidakseimbangan Kelas
Dataset memiliki distribusi kelas yang tidak seimbang, dengan rincian sebagai berikut:
- **Negatif**: 634 data
- **Positif**: 97 data

Untuk menghindari model yang bias terhadap kelas mayoritas, dilakukan penyeimbangan data menggunakan metode **oversampling dengan SMOTE**, sehingga diperoleh distribusi data sebagai berikut:
- **Negatif**: 634 data
- **Positif**: 634 data

---

## Model Machine Learning

### Support Vector Machine (SVM)
Model SVM diimplementasikan menggunakan library `scikit-learn`. Model ini memperoleh **akurasi sebesar 98%** dengan confusion matrix seperti pada gambar berikut.
  
<img width="567" height="490" alt="Confusion Matrix SVM" src="https://github.com/user-attachments/assets/50372045-40da-4598-8142-f480c3db1975" />

---

### Multinomial Naive Bayes (MNB)
Model Multinomial Naive Bayes diimplementasikan menggunakan library `scikit-learn`. Model ini memperoleh **akurasi sebesar 91%** dengan confusion matrix sebagai berikut.
  
<img width="567" height="490" alt="Confusion Matrix MNB" src="https://github.com/user-attachments/assets/9d347ba5-c26a-4df4-942d-793c08e61a6f" />

---

### XGBoost
Model XGBoost diimplementasikan menggunakan library `xgboost`. Sebelum proses training, label sentimen diubah menggunakan **Label Encoder**. Model ini memperoleh **akurasi sebesar 87%** dengan confusion matrix sebagai berikut.
  
<img width="567" height="490" alt="Confusion Matrix XGBoost" src="https://github.com/user-attachments/assets/3ef2f840-bf7c-42b7-a3e0-21ef622dbf60" />

---

### Logistic Regression
Model Logistic Regression diimplementasikan menggunakan library `scikit-learn`. Model ini memperoleh **akurasi sebesar 91%** dengan confusion matrix sebagai berikut.
  
<img width="567" height="490" alt="Confusion Matrix Logistic Regression" src="https://github.com/user-attachments/assets/52e6f7d8-6301-41d0-983e-0775cfab0673" />

---

## Evaluasi Model
Dari keempat model yang diuji, **Logistic Regression dipilih sebagai model terbaik**. Meskipun SVM menghasilkan akurasi tertinggi sebesar 98%, model tersebut **diindikasikan mengalami overfitting**, mengingat performa yang terlalu tinggi dibandingkan model lainnya.

Logistic Regression dipilih karena memberikan **performa yang stabil dan lebih general**, dengan akurasi tinggi serta keseimbangan yang baik antara precision dan recall.

---

## Visualisasi Hasil Analisis

### Analisis Umum
Visualisasi wordcloud secara umum menunjukkan bahwa masyarakat banyak membicarakan kata-kata seperti **sampah**, **solusi**, **perintah**, **buang**, **rumah**, **masyarakat**, dan **Bali**.

<img width="795" height="820" alt="Wordcloud Umum" src="https://github.com/user-attachments/assets/282a2a4a-d719-4628-96a9-d6997149161c" />

---

### Analisis Sentimen Positif
Wordcloud sentimen positif menunjukkan bahwa masyarakat cenderung membahas topik seperti **solusi**, **penting**, **pemerintah**, **biopori**, **kompos**, **sampah organik**, dan **pengelolaan plastik**.

<img width="795" height="820" alt="Wordcloud Positif" src="https://github.com/user-attachments/assets/c57f273a-d90d-47c6-8803-7335271623a5" />

---

### Analisis Sentimen Negatif
Wordcloud sentimen negatif menunjukkan bahwa masyarakat banyak mengungkapkan kekhawatiran terkait **pembuangan sampah**, **kebijakan**, **perintah**, serta dampak terhadap **masyarakat dan lingkungan di Bali**.

<img width="795" height="820" alt="Wordcloud Negatif" src="https://github.com/user-attachments/assets/89c414bb-64a1-4fb6-aff1-5972c04eb57b" />

---

## Kesimpulan
Berdasarkan hasil eksperimen yang telah dilakukan, analisis sentimen menggunakan algoritma **Logistic Regression** memberikan performa yang baik dengan akurasi mencapai **±91–92%**. Hasil visualisasi wordcloud menunjukkan bahwa mayoritas masyarakat menyoroti kebutuhan akan **solusi konkret** dari pemerintah terkait penutupan TPA Suwung.

Berdasarkan hasil analisis sentimen tersebut, dapat disimpulkan bahwa **isu penutupan TPA Suwung tidak memberikan dampak negatif yang signifikan terhadap persepsi masyarakat Kota Denpasar**, melainkan mendorong diskusi yang bersifat solutif.

---

## Hasil Inference Menggunakan Streamlit
Model terbaik telah diimplementasikan dan dideploy menggunakan **Streamlit**, sehingga dapat digunakan untuk melakukan inferensi sentimen secara real-time melalui tautan berikut:

🔗 https://sistem-klasifikasi-sentimen-isu-publik.streamlit.app/

<img width="1919" height="1124" alt="Streamlit App 1" src="https://github.com/user-attachments/assets/368db1f1-907d-4f96-9654-fc5bf32e1d9f" />
<img width="1919" height="1127" alt="Streamlit App 2" src="https://github.com/user-attachments/assets/4c0e0dde-5812-4037-a738-226a5b35a20f" />
