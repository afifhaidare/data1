import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Function to load data (adjust the path as needed)
@st.cache
def load_data():
    data = pd.read_csv('hour.csv')  # Make sure to use your actual data file path
    return data

# Function to plot hourly counts
def plot_hourly_counts(data):
    hourly_counts = data.groupby('hr')['cnt'].mean()
    colors = ['red' if hour in [6, 7, 8, 9, 17, 18, 19] else 'lightgreen' for hour in hourly_counts.index]
    
    plt.figure(figsize=(12, 6))
    hourly_counts.plot(kind="bar", color=colors, title='Rata-Rata Penyewaan Sepeda Per Jam', ylabel='Jumlah Rata-Rata', xlabel='Jam')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.xticks(rotation=0)
    st.pyplot(plt)

# Streamlit UI
def main():
    st.title('Bike Rental Data Visualization')

    data = load_data()

    if st.checkbox('Show raw data'):
        st.write(data)

    st.subheader('Average Bike Rentals per Hour')
    plot_hourly_counts(data)

if __name__ == "__main__":
    main()
