import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns

def georeview(customersdf,ordersdf, geolocationdf, orderreviewdf):
    customer_order_df= pd.merge(
      left = ordersdf,
      right = customersdf,
      how = 'left',
      left_on = 'customer_id',
      right_on = 'customer_id'
      )
    review_df = pd.merge(
      left = customer_order_df,
      right = orderreviewdf,
      how = 'left',
      left_on = 'order_id',
      right_on = 'order_id'
      )
    georeview_df = pd.merge(
      left = review_df,
      right =geolocationdf,
      how = 'left',
      left_on = 'customer_zip_code_prefix',
      right_on = 'geolocation_zip_code_prefix')
   
    georeview_df['order_approved_at']=pd.to_datetime(georeview_df['order_approved_at'])
    georeview_df['order_delivered_carrier_date']=pd.to_datetime(georeview_df['order_delivered_carrier_date'])
    georeview_df['order_delivered_customer_date']=pd.to_datetime(georeview_df['order_delivered_customer_date'])
    georeview_df['durasi_pengiriman'] = (georeview_df['order_delivered_customer_date']
                                     - georeview_df['order_approved_at']).dt.days
  


    return georeview_df


def ordertime(ordersdf,customersdf,orderitemdf,productdf):
  customer_order_df= pd.merge(
    left = ordersdf,
    right = customersdf,
    how = 'left',
    left_on = 'customer_id',
    right_on = 'customer_id'
    )
  order_items_df = pd.merge(
    left = orderitemdf,
    right = productdf,
    how = 'left',
    left_on = 'product_id',
    right_on = 'product_id'
    )
  order_time_df = pd.merge(
    left = order_items_df,
    right = ordersdf,
    how ='left',
    left_on = 'order_id',
    right_on = 'order_id'
  )
 
  order_time_df['order_purchase_timestamp'] = pd.to_datetime(order_time_df['order_purchase_timestamp'])


  order_time_df['tanggal_order'] = order_time_df['order_purchase_timestamp'].dt.date
  order_time_df['perbulan'] = order_time_df['order_purchase_timestamp'].dt.to_period("M")
  order_time_df['perhari'] = order_time_df['order_purchase_timestamp'].dt.day_name()
 
  return order_time_df


def plot_review(georeview_df):
  
  rata_rata_review=georeview_df.groupby('durasi_pengiriman')['review_score'].mean().reset_index()
  fig,ax=plt.subplots(figsize=(10,5))
  sns.lineplot(data=rata_rata_review, x='durasi_pengiriman',y='review_score',marker='o',ax=ax)
  ax.set_title('Rata - Rata Review Score berdasarkan Durasi Pengiriman')
  ax.set_xlabel('Durasi Pengiriman')
  ax.set_ylabel('Rata-Rata Review Score')
  return fig


def plot_review_jarak(georeview_df):
  georeview_df['kategori_jarak'] = georeview_df['durasi_pengiriman'].apply(
    lambda x: 'jauh' if x>3 else 'dekat')
  fig,ax=plt.subplots(figsize=(10,5))
  sns.boxplot(x=georeview_df['kategori_jarak'], y=georeview_df['review_score'], ax=ax)
  ax.set_title('Distribusi Tingkat Kepuasan Pelanggan berdasarkan Kategori Jarak')
  ax.set_xlabel('Kategori Jarak')
  ax.set_ylabel('Review Score')
  return fig


def scatter_review(georeview_df):
  fig, ax = plt.subplots(figsize=(10,5))
  sns.scatterplot(x=georeview_df['durasi_pengiriman'], y=georeview_df['review_score'], alpha=0.2, ax=ax)
  ax.set_title('Scatterplot Jarak vs Review Score')
  ax.set_xlabel('Durasi Pengiriman')
  ax.set_ylabel('Rata - Rata Review Score')
  ax.grid(True)
  return fig


def plot_trend_harian(trend_perhari):
  trend_perhari_urutan = trend_perhari.sort_values(by='jumlah_pesanan', ascending=True)
  plt.figure(figsize=(10,5))
  sns.lineplot(data=trend_perhari_urutan, x='perhari', y='jumlah_pesanan')
  plt.title('Tren Jumlah Pesanan Harian')
  plt.xticks(rotation=50)
  plt.xlabel('Harian')
  plt.ylabel('Jumlah Order')
  plt.grid()
  return plt.gcf()


def plot_trend_bulanan(trend_bulanan):
  trend_bulanan['perbulan']=pd.to_datetime(trend_bulanan['perbulan'])
  trend_bulanan['tahun'] = trend_bulanan['perbulan'].dt.year
  trend_bulanan['bulan'] = trend_bulanan['perbulan'].dt.month
  trend_bulanan['jumlah_pesanan']=pd.to_numeric(trend_bulanan['jumlah_pesanan'])
  heatmapdf = trend_bulanan.pivot_table(index='bulan',columns='tahun',values='jumlah_pesanan',aggfunc='sum')
  plt.figure(figsize=(10,5))
  sns.heatmap(heatmapdf,cmap='Blues',annot=True,fmt='.0f',linewidths=0.5)
  plt.title('Heatmap Jumlah Pemesanan per Bulan')
  plt.xlabel('Tahun')
  plt.ylabel('Bulan')
  plt.yticks(rotation=0)
  return plt.gcf()


def plot_trend_status(order_time_df):
  trend = order_time_df.groupby(['perbulan','order_status'])['order_id'].count().reset_index()
  fig, ax = plt.subplots(figsize=(15,5))
  sns.barplot(data=trend, x='perbulan', y='order_id', hue='order_status', ax=ax)
  ax.set_title('Jumlah Order berdasarkan Status per Bulan')
  ax.set_xlabel('Per Bulan')
  ax.set_ylabel('Jumlah Order')
  plt.xticks(rotation=50)
  plt.yscale('log')
  return fig




def main():
  st.title('Analisis Kepuasan Pelanggan berdasarkan Durasi Pengiriman dan Pola Pembelian Produk')
 
  customersdf = pd.read_csv('customers_dataset.csv', dtype={'customer_id': 'category'})
  ordersdf = pd.read_csv('orders_dataset.csv', dtype={'order_id': 'category', 'customer_id': 'category'})
  geolocationdf = pd.read_csv('geolocation_dataset.csv', dtype={'geolocation_zip_code_prefix': 'category'})
  orderreviewdf = pd.read_csv('order_reviews_dataset.csv', dtype={'order_id': 'category'})
  orderitemdf = pd.read_csv('order_items_dataset.csv', dtype={'order_id': 'category', 'product_id': 'category'})
  productdf = pd.read_csv('products_dataset.csv', dtype={'product_id': 'category'})
 
  georeview_df = georeview(customersdf, ordersdf, geolocationdf, orderreviewdf)
  order_time_df = ordertime(ordersdf,customersdf,orderitemdf,productdf)

  trend_bulanan = order_time_df.groupby('perbulan').agg(jumlah_pesanan=('order_id','count')).reset_index().astype(str)
  trend_perhari = order_time_df.groupby('perhari').agg(jumlah_pesanan=('order_id','count')).reset_index()

  with st.sidebar:
      section = st.selectbox("Pilih Analisis", ["Distribusi Kepuasan", "Tren Pesanan"])
  if section == "Distribusi Kepuasan":
            st.write("Distribusi Tingkat Kepuasan berdasarkan Durasi")
            data_section = st.selectbox("Pilih Data atau Visualisasi", ["Data", "Visualisasi"])
            if data_section == "Data":
                st.write(georeview_df.head(20))  # Menampilkan data dengan benar
            else:
                vis_type = st.selectbox("Pilih Visualisasi", ["Rata-Rata Rate berdasarkan Durasi Pengiriman", "Boxplot", "Scatterplot"])
                if vis_type == "Rata-Rata Rate berdasarkan Durasi Pengiriman":
                    st.write("Menampilkan plot review")
                    st.pyplot(plot_review(georeview_df))
                elif vis_type == "Boxplot":
                    st.write("Menampilkan boxplot")
                    st.pyplot(plot_review_jarak(georeview_df))
                elif vis_type == "Scatterplot":
                    st.write("Menampilkan scatterplot")
                    st.pyplot(scatter_review(georeview_df))
        
  else:
            rentang_waktu = st.date_input("Pilih Rentang Tanggal berdasarkan Tanggal Pembayaran", [])
            if len(rentang_waktu) == 2:
              start_date, end_date = rentang_waktu
              with st.expander("Trend Pesanan"):
                  data_section = st.selectbox("Pilih Data atau Visualisasi", ["Data", "Visualisasi"])
                  if data_section == "Data":
                      st.write(order_time_df[(order_time_df['order_purchase_timestamp'] >= pd.Timestamp(start_date)) & 
                                            (order_time_df['order_purchase_timestamp'] <= pd.Timestamp(end_date))])
                  
                  else:
                      vis_type = st.selectbox("Pilih Visualisasi", ["Tren Jumlah Pesanan Harian", 'Tren Status per Bulan', "Tren Jumlah Pesanan Bulanan"])
                      if vis_type == "Tren Jumlah Pesanan Harian":
                          st.pyplot(plot_trend_harian(trend_perhari))
                      elif vis_type == "Tren Status per Bulan":
                        st.pyplot(plot_trend_status(order_time_df))
                      else:
                          st.pyplot(plot_trend_bulanan(trend_bulanan))
    
          
if __name__ == "__main__":
    main()




