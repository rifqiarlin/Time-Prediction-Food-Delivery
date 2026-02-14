# 🚚 Food Delivery Time Prediction (Lasso Regression)

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://time-prediction-food-delivery.streamlit.app/)
![Scikit-Learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)

Aplikasi berbasis web untuk memprediksi durasi pengiriman makanan secara real-time. Proyek ini mendemonstrasikan implementasi **Lasso Regression** dengan optimasi **GridSearchCV** untuk menghasilkan prediksi yang akurat dan efisien.

---

## 🔗 Live Demo
Coba aplikasi langsung di sini:  
👉 **[https://time-prediction-food-delivery.streamlit.app/](https://time-prediction-food-delivery.streamlit.app/)**

---

## 🎯 Ringkasan Proyek
Model ini dikembangkan untuk membantu operasional logistik makanan dalam mengestimasi waktu tiba (ETA). Algoritma Lasso dipilih karena kemampuannya dalam melakukan seleksi fitur otomatis (penyusutan koefisien), sehingga hanya variabel yang paling berpengaruh yang digunakan dalam prediksi akhir.

### 🛠️ Fitur Teknis
- **Model Tuning:** Hyperparameter dioptimalkan menggunakan pencarian grid (Alpha parameter).
- **Interactive Input:** Menggunakan slider (drag line) untuk variabel kontinu.
- **Robust Handling:** Penanganan data kategori (Cuaca, Trafik, Waktu) menggunakan pipeline yang terintegrasi.

---

## 📊 Dataset & Fitur
Data input yang digunakan oleh model meliputi:
- **Numerik:** Jarak (km), Waktu Persiapan Restoran (menit), Pengalaman Kurir (tahun).
- **Kategorikal:** Cuaca (Rainy, Foggy, dll), Level Trafik, Waktu Hari, dan Jenis Kendaraan.

---
