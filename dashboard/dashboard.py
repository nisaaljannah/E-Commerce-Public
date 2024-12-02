import pandas as pd
import plotly.express as px
import streamlit as st

# Memuat dataset
orders_dataset = pd.read_csv("main_data.csv")

# Memuat data yang diperlukan untuk analisis
orders_dataset['order_purchase_timestamp'] = pd.to_datetime(orders_dataset['order_purchase_timestamp'])
monthly_orders = orders_dataset['order_purchase_timestamp'].apply(pd.to_datetime).dt.to_period('M').value_counts().sort_index()

# Judul Aplikasi
st.title("E-Commerce Dashboard")

# Dropdown untuk memilih visualisasi
visualization = st.selectbox(
    "Pilih Visualisasi",
    ("Distribusi Jenis Pembayaran", "Distribusi Status Pesanan")
)

# Membuat Grafik Berdasarkan Pilihan
if visualization == "Distribusi Jenis Pembayaran":
    payment_counts = orders_dataset["payment_type"].value_counts().reset_index()
    payment_counts.columns = ['payment_type', 'count']
    fig = px.bar(payment_counts, x="payment_type", y="count", labels={"payment_type": "Jenis Pembayaran", "count": "Jumlah"})
    st.plotly_chart(fig)

elif visualization == "Distribusi Status Pesanan":
    order_status_counts = orders_dataset["order_status"].value_counts().reset_index()
    order_status_counts.columns = ['order_status', 'count']
    fig = px.bar(order_status_counts, x="order_status", y="count", labels={"order_status": "Status Pesanan", "count": "Jumlah"})
    st.plotly_chart(fig)

# Histogram untuk distribusi pembayaran
st.subheader("Distribusi Nilai Pembayaran")
fig2 = px.histogram(orders_dataset, x="payment_value", nbins=30, title="Distribusi Nilai Pembayaran")
st.plotly_chart(fig2)

# Tren Pembelian per Bulan
st.subheader("Tren Pembelian per Bulan")
fig3 = px.line(
    x=monthly_orders.index.astype(str),
    y=monthly_orders.values,
    labels={"x": "Bulan", "y": "Jumlah Pembelian"},
    title="Jumlah Pembelian per Bulan"
)
st.plotly_chart(fig3)
