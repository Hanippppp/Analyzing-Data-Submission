import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Judul aplikasi
st.title('Analisis Data Penggunaan Sepeda')

# Memuat dataset
day_data = pd.read_csv('dataset/day.csv')
hour_data = pd.read_csv('dataset/hour.csv')

# Mengubah kolom tanggal menjadi tipe datetime
day_data['dteday'] = pd.to_datetime(day_data['dteday'])
day_data.set_index('dteday', inplace=True)
monthly_usage = day_data.resample('M').sum()
correlation_matrix = day_data.corr()

# Visualisasi tren penggunaan sepeda
st.subheader('Tren Penggunaan Sepeda dalam Setahun')
fig, ax = plt.subplots(figsize=(12, 6))
ax.plot(monthly_usage.index, monthly_usage['cnt'], marker='o')
ax.set_title('Tren Penggunaan Sepeda dalam Setahun')
ax.set_xlabel('Bulan')
ax.set_ylabel('Jumlah Penggunaan Sepeda')
ax.grid(True)
st.pyplot(fig)

# Visualisasi faktor-faktor yang mempengaruhi penggunaan sepeda
st.subheader('Pengaruh Faktor-Faktor terhadap Penggunaan Sepeda')
fig, ax = plt.subplots(figsize=(12, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', ax=ax)
ax.set_title('Matriks Korelasi Faktor-Faktor yang Mempengaruhi Penggunaan Sepeda')
st.pyplot(fig)

# Scatter plot suhu dan jumlah penggunaan sepeda
st.subheader('Pengaruh Suhu terhadap Jumlah Penggunaan Sepeda')
fig, ax = plt.subplots(figsize=(10, 6))
sns.scatterplot(x='temp', y='cnt', data=day_data, ax=ax)
ax.set_title('Pengaruh Suhu terhadap Jumlah Penggunaan Sepeda')
ax.set_xlabel('Suhu (Normalisasi)')
ax.set_ylabel('Jumlah Penggunaan Sepeda')
ax.grid(True)
st.pyplot(fig)