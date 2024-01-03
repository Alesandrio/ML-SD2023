# Импорт модулей
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from stocks_data import StockDataDownloader
stock_downloader = StockDataDownloader()
from lin_model import Predictor

# Конфиг в коде
tickers = ["AAPL", "AMZN", "BABA", "GOOGL", "JNJ", "META", "MSFT", "NFLX", "NVDA", "TSLA"]
target_column = 'price'

# Получение котировок акций по тикерам
stocks_data = stock_downloader.download_multiple_stocks_data(tickers)
for ticker, data_frame in stocks_data.items():
    # Используем globals() для создания переменной
    globals()[f"{ticker}"] = data_frame

# Прогноз курса акций компаний на различные временные периоды
window_sizes = np.arange(2, 15)
test_size = 3
ds_predict_3_day, today = Predictor.predict_sma_tickers(tickers, stocks_data, target_column, window_sizes, test_size)

window_sizes = np.arange(3, 18)
test_size = 7
ds_predict_7_day, today = Predictor.predict_sma_tickers(tickers, stocks_data, target_column, window_sizes, test_size)

window_sizes = np.arange(5, 25)
test_size = 14
ds_predict_14_day, today = Predictor.predict_sma_tickers(tickers, stocks_data, target_column, window_sizes, test_size)

window_sizes = np.arange(15, 35)
test_size = 31
ds_predict_31_day, today = Predictor.predict_sma_tickers(tickers, stocks_data, target_column, window_sizes, test_size)

