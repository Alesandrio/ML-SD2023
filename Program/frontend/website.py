import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

import streamlit as st

# Определение страницы "О проекте"
def about_project():
    st.title("Прогнозирование акций с помощью статистических моделей")
    st.write("Данный проект предоставляет прогнозы акций на основе статистических моделей.")
    st.write("Это не является инвестиционной рекомендацией.")

# Определение страниц с акциями
def stock_page(stock_symbol):
    st.write(f"*Не является инвестиционной рекомендацией* для {stock_symbol}")

# Главная функция
def main():
    st.sidebar.title("Навигация")
    pages = ["О проекте", "AAPL", "AMZN", "BABA", "GOOGL", "JNJ", "META", "MSFT", "NFLX", "NVDA", "TSLA"]
    selected_page = st.sidebar.radio("Выберите страницу", pages)

    if selected_page == "О проекте":
        about_project()
    else:
        stock_page(selected_page)

if __name__ == "__main__":
    main()


# Config
name_company = f'Apple Inc (AAPL)'
file_path_3_day = 'ML-SD2023\\Program\\data_predictions\\AAPL_3_day.csv'
file_path_7_day = 'ML-SD2023\\Program\\data_predictions\\AAPL_7_day.csv'
file_path_14_day = 'ML-SD2023\\Program\\data_predictions\\AAPL_14_day.csv'
file_path_31_day = 'ML-SD2023\\Program\\data_predictions\\AAPL_31_day.csv'
file_path_today = 'ML-SD2023\\Program\\data_predictions\\today.csv'
df_3_day = pd.read_csv(file_path_3_day)
df_7_day = pd.read_csv(file_path_7_day)
df_14_day = pd.read_csv(file_path_14_day)
df_31_day = pd.read_csv(file_path_31_day)
today_date = pd.read_csv(file_path_today)
today = today_date['date'].iloc[0]

# Sidebar
page = st.sidebar.selectbox("Выберите страницу", ["О проекте", "AAPL", "AMZN", "BABA", "GOOGL", "JNJ", "META", "MSFT", "NFLX", "NVDA", "TSLA"])

# О проекте
if page == "О проекте":
    st.title("Проект: Прогнозирование акций с помощью статистических моделей")
    st.write("Проект разработан для демонстрации возможностей прогнозирования акций с использованием статистических моделей.")
    st.write("Не является инвестиционной рекомендацией.")

# AAPL
if page == "AAPL":
    period = st.radio("Выберите период прогноза", ["3 дня", "7 дней", "14 дней", "31 день"])

    if period == "3 дня":
        df_future = df_3_day
    elif period == "7 дней":
        df_future = df_7_day
    elif period == "14 дней":
        df_future = df_14_day
    elif period == "31 день":
        df_future = df_31_day

    name_period_company = f'{name_company} - прогноз на {period}'
    
    fig, ax = plt.subplots(figsize=(11, 6))
    plt.style.use('https://github.com/dhaitz/matplotlib-stylesheets/raw/master/pitayasmoothie-dark.mplstyle')
    plt.plot(df_future['date'], df_future['target'], label='Rate', color='blue', linewidth=3)
    plt.plot(df_future['date'], df_future['predict'], label='Predict', color='red', linewidth=3)
    train_end_date = pd.to_datetime(today)
    ax.axvline(today, color='black', linestyle='--')
    plt.xticks(rotation=45)
    plt.legend(loc='upper right')
    plt.title(name_period_company, loc="center", size=18, weight='bold')
    st.pyplot(fig)
