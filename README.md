# Analisis Kepuasan Pelanggan berdasarkan Durasi Pengiriman dan Pola Pembelian Produk

## 📑 Deskripsi
Aplikasi ini dibuat dengan **Streamlit** untuk menganalisis tingkat kepuasan pelanggan berdasarkan kondisi jarak dan melihat pola pembelian produk. 

🔗[Open in Streamlit](https://dashboard-ecommerce-public.streamlit.app/)

## 🗂 Dataset
Dataset yang digunakan pada aplikasi ini adalah:
   1. 'customers_dataset.csv' berisi data pelanggan
   2. 'orders_dataset.csv' berisi data pesanan
   3. 'geolocation_dataset.csv' berisi data lokasi pelanggan
   4. 'order_reviews_dataset.csv' berisi data ulasan pelanggan
   5. 'products_dataset.csv' berisi data produk

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
   1. **Rata - Rata Tingkat Kepuasan Pelanggan berdasarkan Durasi Pengiriman** : melihat tren rata - rata tingkat kepuasan pelangan berdasarkan durasi pengiriman. 
   2. **Boxplot Tingkat Kepuasan berdasarkan Kategori Jarak** : melihat variasi tingkat kepuasan pelanggan berdasarkan kategori jarak.
   3. **Scatterplot Jarak vs Review Score**: melihat hubungan antara tingkat kepuasan dengan kategori jarak.
   4. **Tren Jumlah Pesanan Harian**: melihat pola pesanan berdasarkan harian.
   5. **Heatmap Tren Bulanan**: melihat pola jumlah pemesanan berdasarkan bulan.
   6. **Jumlah Order Berdasarkan Status per Bulan**: menunjukkan tren jumlah pemesanan berdasarkan status. 
