# Импорт библиотек
import pandas as pd
import os

# Импорт модулей
from stocks_data import StockDataDownloader
from lin_model import Predictor

# Импорт переменных
from config import (
    tickers,
    target_column,
    window_sizes_3_day,
    test_size_3_day,
    window_sizes_7_day,
    test_size_7_day,
    window_sizes_14_day,
    test_size_14_day,
    window_sizes_31_day,
    test_size_31_day
)

##############################################################################################################################

# Получение котировок акций по тикерам
stock_downloader = StockDataDownloader()
stocks_data = stock_downloader.download_multiple_stocks_data(tickers)
for ticker, data_frame in stocks_data.items():
    globals()[f"{ticker}"] = data_frame

##############################################################################################################################

# Функция для рассчета прогнозных значений
def calculate_and_save_predictions():
    ds_predict_3_day, today = Predictor.predict_sma_tickers(tickers, stocks_data, target_column, window_sizes_3_day, test_size_3_day)
    ds_predict_7_day, today = Predictor.predict_sma_tickers(tickers, stocks_data, target_column, window_sizes_7_day, test_size_7_day)
    ds_predict_14_day, today = Predictor.predict_sma_tickers(tickers, stocks_data, target_column, window_sizes_14_day, test_size_14_day)
    ds_predict_31_day, today = Predictor.predict_sma_tickers(tickers, stocks_data, target_column, window_sizes_31_day, test_size_31_day)
    return ds_predict_3_day, ds_predict_7_day, ds_predict_14_day, ds_predict_31_day, today

# Проверяем, были ли данные уже рассчитаны и сохранены
try:
    ds_predict_3_day, ds_predict_7_day, ds_predict_14_day, ds_predict_31_day, today
except NameError:
    # Если переменные не определены, значит данные еще не были рассчитаны
    ds_predict_3_day, ds_predict_7_day, ds_predict_14_day, ds_predict_31_day, today = calculate_and_save_predictions()

##############################################################################################################################

# Путь к папке для сохранения файлов
save_folder_path = 'ML-SD2023\\Program\\data_predictions'

# Проверяем, существует ли папка, если нет, создаем ее
if not os.path.exists(save_folder_path):
    os.makedirs(save_folder_path)

for ticker in tickers:
    # Создаем переменные с именами, содержащими тикеры и временные интервалы
    globals()[f'{ticker}_3_day'] = pd.DataFrame(ds_predict_3_day[ticker]['predict'])
    globals()[f'{ticker}_7_day'] = pd.DataFrame(ds_predict_7_day[ticker]['predict'])
    globals()[f'{ticker}_14_day'] = pd.DataFrame(ds_predict_14_day[ticker]['predict'])
    globals()[f'{ticker}_31_day'] = pd.DataFrame(ds_predict_31_day[ticker]['predict'])
    # Создаем пути для сохранения файлов
    file_path_3_day = os.path.join(save_folder_path, f'{ticker}_3_day.csv')
    file_path_7_day = os.path.join(save_folder_path, f'{ticker}_7_day.csv')
    file_path_14_day = os.path.join(save_folder_path, f'{ticker}_14_day.csv')
    file_path_31_day = os.path.join(save_folder_path, f'{ticker}_31_day.csv')
    # Сохраняем датафреймы в CSV файлы
    globals()[f'{ticker}_3_day'].to_csv(file_path_3_day, index=False)
    globals()[f'{ticker}_7_day'].to_csv(file_path_7_day, index=False)
    globals()[f'{ticker}_14_day'].to_csv(file_path_14_day, index=False)
    globals()[f'{ticker}_31_day'].to_csv(file_path_31_day, index=False)

today_df = pd.DataFrame({'date': [today]})
file_path_today = os.path.join(save_folder_path, 'today.csv')
today_df.to_csv(file_path_today, index=False)