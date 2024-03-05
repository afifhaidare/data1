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
    plt.title('Temperature vs. Bike Rental Count')
    plt.xlabel('Normalized Temperature')
    plt.ylabel('Rental Count')

    # Windspeed vs. Count
    plt.subplot(1, 2, 2)  # 1 row, 2 columns, 2nd subplot
    sns.regplot(x='windspeed', y='cnt', data=data, scatter_kws={'alpha':0.5}, line_kws={'color': 'blue'})
    plt.title('Windspeed vs. Bike Rental Count')
    plt.xlabel('Normalized Windspeed')
    plt.ylabel('Rental Count')

    st.pyplot(plt)

# Streamlit UI
def main():
    st.title('Bike Rental Data Visualization')

    data = load_data()

    if st.checkbox('Show raw data'):
        st.write(data)

    st.subheader('Average Bike Rentals per Hour')
    plot_hourly_counts(data)

    st.subheader('Temperature and Windspeed vs. Bike Rental Count')
    plot_scatter_plots(data)

if __name__ == "__main__":
    main()
