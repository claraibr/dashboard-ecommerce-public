# Analisis Kepuasan Pelanggan berdasarkan Durasi Pengiriman dan Pola Pembelian Produk

## 📑 Deskripsi
Aplikasi ini dibuat dengan **Streamlit** untuk menganalisis tingkat kepuasan pelanggan berdasarkan kondisi jarak dan melihat pola pembelian produk. 

[![Open in Streamlit](https://humble-guacamole-69w9rg4qv7wjf4v6v-8501.app.github.dev/)]

## 🗂 Dataset
Dataset yang digunakan pada aplikasi ini adalah:
-'customers_dataset.csv' berisi data pelanggan
-'orders_dataset.csv' berisi data pesanan
-'geolocation_dataset.csv' berisi data lokasi pelanggan
-'order_reviews_dataset.csv' berisi data ulasan pelanggan
-'products_dataset.csv' berisi data produk

## How to run it on your own machine

1. Install the requirements

   ```
   $ pip install streamlit pandas matplotlib seaborn
   ```

2. Run the app

   ```
   $ streamlit run streamlit_app.py
   ```

## ⚙ Fitur
- **Rata - Rata Tingkat Kepuasan Pelanggan berdasarkan Durasi Pengiriman** : melihat tren rata - rata tingkat kepuasan pelangan berdasarkan durasi pengiriman. 
- **Boxplot Tingkat Kepuasan berdasarkan Kategori Jarak** : melihat variasi tingkat kepuasan pelanggan berdasarkan kategori jarak.
- **Scatterplot Jarak vs Review Score**: melihat hubungan antara tingkat kepuasan dengan kategori jarak.
-**Tren Jumlah Pesanan Harian**: melihat pola pesanan berdasarkan harian.
-**Heatmap Tren Bulanan**: melihat pola jumlah pemesanan berdasarkan bulan.
-**Jumlah Order Berdasarkan Status per Bulan**: menunjukkan tren jumlah pemesanan berdasarkan status. 
