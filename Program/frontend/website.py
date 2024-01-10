import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


# Определение страницы "О проекте"
def about_project():
    st.title("Прогнозирование акций с помощью статистических моделей")
    st.write("Данный проект предоставляет прогнозы акций на основе статистических моделей.")
    st.write("Прогнозы, представленные в данном веб-сервисе, не являются инвестиционными рекомендациями!")


# Определение страницы с акциями
def stock_page(stock_symbol):
    st.title(f"{stock_symbol} - Прогноз акций")
    st.write(f"*Не является инвестиционной рекомендацией* для {stock_symbol}")

    # Добавляем график по кнопке "Прогноз на 3 дня"
    if st.button("Прогноз на 3 дня"):
        # Импорт данных
        file_path_3_day = f'ML-SD2023\\Program\\data_predictions\\{stock_symbol}_3_day.csv'
        file_path_today = 'ML-SD2023\\Program\\data_predictions\\today.csv'
        df_3_day = pd.read_csv(file_path_3_day)
        today_date = pd.read_csv(file_path_today)
        today = today_date['date'].iloc[0]
        # Построение графика
        df_future = df_3_day
        name_priod_company = f'{stock_symbol} - прогноз на 3 дня'
        fig, ax = plt.subplots(figsize=(11, 6))
        plt.style.use('https://github.com/dhaitz/matplotlib-stylesheets/raw/master/pitayasmoothie-dark.mplstyle')
        plt.plot(df_future['date'], df_future['target'], label='Rate', color='blue', linewidth=3)
        plt.plot(df_future['date'], df_future['predict'], label='Predict', color='red', linewidth=3)
        train_end_date = pd.to_datetime(today)
        ax.axvline(today, color='black', linestyle='--')
        plt.xticks(rotation=45)
        plt.legend(loc='upper right')
        plt.title(name_priod_company, loc="center", size=18, weight='bold')
        st.pyplot(fig)
    
        # Добавляем график по кнопке "Прогноз на 7 дней"
    if st.button("Прогноз на 7 дней"):
        # Импорт данных
        file_path_7_day = f'ML-SD2023\\Program\\data_predictions\\{stock_symbol}_7_day.csv'
        file_path_today = 'ML-SD2023\\Program\\data_predictions\\today.csv'
        df_7_day = pd.read_csv(file_path_7_day)
        today_date = pd.read_csv(file_path_today)
        today = today_date['date'].iloc[0]
        # Построение графика
        df_future = df_7_day
        name_priod_company = f'{stock_symbol} - прогноз на 7 дней'
        fig, ax = plt.subplots(figsize=(11, 6))
        plt.style.use('https://github.com/dhaitz/matplotlib-stylesheets/raw/master/pitayasmoothie-dark.mplstyle')
        plt.plot(df_future['date'], df_future['target'], label='Rate', color='blue', linewidth=3)
        plt.plot(df_future['date'], df_future['predict'], label='Predict', color='red', linewidth=3)
        train_end_date = pd.to_datetime(today)
        ax.axvline(today, color='black', linestyle='--')
        plt.xticks(rotation=45)
        plt.legend(loc='upper right')
        plt.title(name_priod_company, loc="center", size=18, weight='bold')
        st.pyplot(fig)

        # Добавляем график по кнопке "Прогноз на 14 дней"
    if st.button("Прогноз на 14 дней"):
        # Импорт данных
        file_path_14_day = f'ML-SD2023\\Program\\data_predictions\\{stock_symbol}_14_day.csv'
        file_path_today = 'ML-SD2023\\Program\\data_predictions\\today.csv'
        df_14_day = pd.read_csv(file_path_14_day)
        today_date = pd.read_csv(file_path_today)
        today = today_date['date'].iloc[0]
        # Построение графика
        df_future = df_14_day
        name_priod_company = f'{stock_symbol} - прогноз на 14 дней'
        fig, ax = plt.subplots(figsize=(11, 6))
        plt.style.use('https://github.com/dhaitz/matplotlib-stylesheets/raw/master/pitayasmoothie-dark.mplstyle')
        plt.plot(df_future['date'], df_future['target'], label='Rate', color='blue', linewidth=3)
        plt.plot(df_future['date'], df_future['predict'], label='Predict', color='red', linewidth=3)
        train_end_date = pd.to_datetime(today)
        ax.axvline(today, color='black', linestyle='--')
        plt.xticks(rotation=45)
        plt.legend(loc='upper right')
        plt.title(name_priod_company, loc="center", size=18, weight='bold')
        st.pyplot(fig)

        # Добавляем график по кнопке "Прогноз на 31 день"
    if st.button("Прогноз на 31 дней"):
        # Импорт данных
        file_path_31_day = f'ML-SD2023\\Program\\data_predictions\\{stock_symbol}_31_day.csv'
        file_path_today = 'ML-SD2023\\Program\\data_predictions\\today.csv'
        df_31_day = pd.read_csv(file_path_31_day)
        today_date = pd.read_csv(file_path_today)
        today = today_date['date'].iloc[0]
        # Построение графика
        df_future = df_31_day
        name_priod_company = f'{stock_symbol} - прогноз на 31 дней'
        fig, ax = plt.subplots(figsize=(11, 6))
        plt.style.use('https://github.com/dhaitz/matplotlib-stylesheets/raw/master/pitayasmoothie-dark.mplstyle')
        plt.plot(df_future['date'], df_future['target'], label='Rate', color='blue', linewidth=3)
        plt.plot(df_future['date'], df_future['predict'], label='Predict', color='red', linewidth=3)
        train_end_date = pd.to_datetime(today)
        ax.axvline(today, color='black', linestyle='--')
        plt.xticks(rotation=45)
        plt.legend(loc='upper right')
        plt.title(name_priod_company, loc="center", size=18, weight='bold')
        st.pyplot(fig)


# Функция запуска страницы
def main():
    st.sidebar.title("Навигация")
    pages = ["О проекте", "AAPL", "AMZN", "BABA", "GOOGL", "JNJ", "META", "MSFT", "NFLX", "NVDA", "TSLA"]
    selected_page = st.sidebar.radio("Выберите страницу", pages)

    if selected_page == "О проекте":
        about_project()
    else:
        st.title("Навигация на странице компании")
        # buttons_html = """
        # <div style="display: flex; justify-content: space-between;">
        #     <button style="margin-right: 10px;">О компании</button>
        #     <button style="margin-right: 10px;">Прогноз на 3 дня</button>
        #     <button style="margin-right: 10px;">Прогноз на 7 дней</button>
        #     <button style="margin-right: 10px;">Прогноз на 14 дней</button>
        #     <button>Прогноз на 31 день</button>
        # </div>
        # """
        # st.markdown(buttons_html, unsafe_allow_html=True)
        stock_page(selected_page)


if __name__ == "__main__":
    main()