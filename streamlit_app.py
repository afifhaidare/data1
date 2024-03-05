import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

@st.cache
def load_data():
    data = pd.read_csv('hour.csv')
    return data

def plot_hourly_counts(data):
    hourly_counts = data.groupby('hr')['cnt'].mean()
    colors = ['red' if hour in [6, 7, 8, 9, 17, 18, 19] else 'lightgreen' for hour in hourly_counts.index]
    
    plt.figure(figsize=(12, 6))
    hourly_counts.plot(kind="bar", color=colors, title='Rata-Rata Penyewaan Sepeda Per Jam', ylabel='Jumlah Rata-Rata', xlabel='Jam')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.xticks(rotation=0)
    st.pyplot(plt)

# Function to plot scatter plots
def plot_scatter_plots(data):
    # Temperature vs. Count
    plt.figure(figsize=(12, 6))
    plt.subplot(1, 2, 1)  # 1 row, 2 columns, 1st subplot
    sns.regplot(x='temp', y='cnt', data=data, scatter_kws={'alpha':0.5}, line_kws={'color': 'red'})
    plt.title('Suhu vs. Penyewaan Sepeda')
    plt.xlabel('Suhu')
    plt.ylabel('Penyewaan Sepeda')

    # Windspeed vs. Count
    plt.subplot(1, 2, 2)  # 1 row, 2 columns, 2nd subplot
    sns.regplot(x='windspeed', y='cnt', data=data, scatter_kws={'alpha':0.5}, line_kws={'color': 'blue'})
    plt.title('Kecepatan Angin vs. Penyewaan Sepeda')
    plt.xlabel('Kecepatan Angin')
    plt.ylabel('Penyewaan Sepeda')

    st.pyplot(plt)

# Streamlit UI
def main():
    st.title('Data Visualisasi Penyewaan Sepeda')

    data = load_data()

    if st.checkbox('Show raw data'):
        st.write(data)

    st.subheader('Rata-Rata Penyewaan Sepeda per Jam')
    plot_hourly_counts(data)
    st.markdown("Kita dapat melihat trend Rush Hour Pagi dan Rush Hour Sore yang lebih tinggi dibandingkan jam lainnya, kita dapat memberikan konklusi bahwa Rush Hour Sore mempunyai trend yang lebih tinggi daripada Rush Hour Pagi, dan kita bisa memberikan saran dan rekomendasi untuk menambahkan kuota sepeda pada Rush Hour Sore. Pada kota ini kita juga bisa melihat bahwa warga tersebut lebih suka menggunakan sepeda pada sore hari dan mungkin menggunakan public transport pada pagi hari.")
    st.subheader('Suhu dan Kecepatan Angin vs. Penyewaan Sepeda')
    plot_scatter_plots(data)
    st.markdown("Kita dapat melihat dari kedua Scatter Graph tersebut bahwa ada trend Positif pada graph Suhu vs Jumlah dan trend Negatif pada graph Kecepatan Angin vs Jumlah. Kita dapat memberikan konklusi semakin tinggi suhu semakin banyak juga jumlah penyewaan sepeda, dan semakin kecil kecepatan angin semakin besar penyewaan sepeda.")
if __name__ == "__main__":
    main()
