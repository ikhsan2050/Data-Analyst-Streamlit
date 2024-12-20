import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
sns.set(style='dark')

# Impor dataset
day = pd.read_csv('day.csv')
day.head()

# Mengganti nama kolom
day.rename(columns={
    'dteday': 'date',
    'yr': 'year',
    'mnth': 'month',
    'weathersit': 'weather_condition',
    'hum': 'humidity',
    'cnt': 'count'
}, inplace=True)

# Mengubah angka menjadi kategori
day['season'] = day['season'].replace({
    1: 'Spring',
    2: 'Summer',
    3: 'Fall',
    4: 'Winter'
})

day['year'] = day['year'].replace({
    0: 2011,
    1: 2012
})

day['month'] = day['month'].replace({
    1: 'January',
    2: 'February',
    3: 'March',
    4: 'April',
    5: 'May',
    6: 'June',
    7: 'July',
    8: 'August',
    9: 'September',
    10: 'October',
    11: 'November',
    12: 'December'
})

day['holiday'] = day['holiday'].replace({
    0: 'No',
    1: 'Yes'
})

day['weekday'] = day['weekday'].replace({
    0: 'Sunday',
    1: 'Monday',
    2: 'Tuesday',
    3: 'Wednesday',
    4: 'Thursday',
    5: 'Friday',
    6: 'Saturday'
})

day['workingday'] = day['workingday'].replace({
    0: 'No',
    1: 'Yes'
})

day['weather_condition']= day['weather_condition'].replace({
    1: 'Clear/Partly Cloudy',
    2: 'Misty/Cloudy',
    3: 'Light Snow/Rain',
    4: 'Severe Weather'
})

with st.sidebar:
    # Menambahkan judul dan subjudul
    st.title('Proyek Analisis Data: Bike Sharing Dataset')
    st.header('Nama: Muhammad Ikhsanudin')
    st.subheader('Email: ikhsan2050@gmail.com')
    st.subheader('ID Dicoding: ikhsan2050')

# Membuat judul dashboard
st.header('Proyek Analisis Data: Bike Sharing Dataset')
st.subheader('Peminjaman Sepeda Berdasarkan Musim')

day.groupby(by='season').agg({
    'count': ['min', 'max','mean','sum']
    }).sort_values(by=('count', 'mean'), ascending=False)

# Diagram pertama
fig = plt.figure(figsize=(10, 6))
ax = sns.barplot(
    x='season',
    y='count',
    data=day,
    errorbar=None,
    hue='season',
    order=day.groupby(['season'])['count'].mean().sort_values().index)
for c in ax.containers:
    ax.bar_label(c)

plt.title('Jumlah Pengguna Sepeda berdasarkan Musim')
plt.xlabel('Musim')
plt.ylabel('Jumlah Pengguna Sepeda')
st.pyplot(fig)

st.write('''
    Berdasarkan visualisasi data menggunakan barplot, dapat dilihat bahwa terdapat pengaruh antara musim terhadap peminjaman sepeda.
    \nMusim gugur (Fall) menjadi musim dengan peminjaman terbesar, diikuti musim panas (Summer), musim dingin (Winter), dan terakhir musim semi (Spring).
''')

# Diagram Kedua
st.subheader('Peminjaman Sepeda Berdasarkan Hari')

fig = plt.figure(figsize=(10, 6))
ax = sns.barplot(
    x='weekday',
    y='count',
    data=day,
    errorbar=None,
    hue='weekday',
    order=day.groupby(['weekday'])['count'].mean().sort_values().index)
for c in ax.containers:
    ax.bar_label(c)

plt.title('Jumlah Pengguna Sepeda berdasarkan Hari')
plt.xlabel('Hari')
plt.ylabel('Jumlah Pengguna Sepeda')
st.pyplot(fig)

st.write('''
    Berdasarkan visualisasi data menggunakan barplot, dapat dilihat bahwa terdapat pengaruh antara hari terhadap peminjaman sepeda.
    Urutan peminjaman sepeda dari yang terkecil hingga terbesar adalah sebagai berikut:
    \nMinggu, Senin, Selasa, Rabu, Sabtu, Kamis, dan Jumat
''')

# Diagram Ketiga
st.subheader('Tren Peminjaman Sepeda pada Tahun 2011 dan 2012')

day['month'] = pd.Categorical(day['month'], categories=[
    'January', 'February', 'March', 'April', 'May', 'June',
    'July', 'August', 'September', 'October', 'November', 'December'], ordered=True)

monthly_counts = day.groupby(by=['month', 'year']).agg({
    'count': 'sum'
}).reset_index()

fig = plt.figure(figsize=(12, 6))
ax = sns.lineplot(
    x='month',
    y='count',
    hue='year',
    data=monthly_counts,
    marker='o',
    palette=sns.color_palette())

plt.title('Jumlah Pengguna Sepeda setiap Bulan pada Tahun 2011 dan 2012')
plt.xlabel('Bulan')
plt.ylabel('Jumlah Pengguna Sepeda')
st.pyplot(fig)

st.write('''
    Berdasarkan visualisasi data menggunakan lineplot, dapat dilihat bahwa:
    \n- Tahun 2012 memiliki jumlah peminjam sepeda lebih banyak daripada Tahun 2011 pada setiap bulannya.
    \n- Pada Tahun 2011, peminjaman tertinggi berada pada bulan Juni dan peminjaman terendah berada pada bulan Januari.
    \n- Pada Tahun 2012, peminjaman tertinggi berada pada bulan September dan peminjaman terendah berada pada bulan Januari.

''')

st.caption('Copyright Mukhamad Ikhsanudin © Dicoding 2024')
