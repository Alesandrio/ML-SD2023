import logging
import yfinance as yf
import time
import yaml
from database_manager import DatabaseManager
from datetime import timedelta
import threading

# Настройка логирования
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


class PriceParser:
    def __init__(self, db_manager, config_path='config.yaml'):
        with open(config_path, 'r') as file:
            config = yaml.safe_load(file)

        self.tickers = config.get('tickers')
        self.timeframe = config.get('timeframe')
        self.period = config.get('period')
        self.db_manager = db_manager
        logger.info("Initializing PriceParser with tickers: %s", self.tickers)
        for company in self.tickers:
            self.check_database(company, timeframe=self.timeframe)

    @staticmethod
    def get_last_candle(ticker_symbol: str, timeframe: str = '15m'):
        """Возвращает последнюю доступную свечу из yfinance

        Parameters
        ----------
        ticker_symbol : str
            'AAPL' - apple inc
            'BTC-USD' - Bitcoin rate

        timeframe:
            “5m”, “15m”, “30m”, “60m”, “1h”

        Returns:
            dict
        """
        ticker = yf.Ticker(ticker_symbol)
        data = ticker.history(period="1d", interval=timeframe)
        last_candle = data.iloc[-2]
        result = dict()
        result['Datetime'] = data.index[-2]
        result['Open'] = last_candle['Open']
        result['High'] = last_candle['High']
        result['Low'] = last_candle['Low']
        result['Close'] = last_candle['Close']
        result['Volume'] = last_candle['Volume']

        return result

    def check_database(self, ticker_symbol: str, timeframe: str = '15m'):
        """При перезапуске скрипта проверяет совпадает ли
        последняя дата в БД и дата в yfinance,
        если нет, то перезаписывает последние данные за period"""
        logger.info("Checking database for ticker: %s", ticker_symbol)
        if self.timeframe == '1m':
            delta = 1
        elif self.timeframe == '5m':
            delta = 5
        elif self.timeframe == '30m':
            delta = 30
        elif self.timeframe == '1h' or self.timeframe == '60m':
            delta = 60
        else:
            delta = 15

        db_name = ticker_symbol + '_' + timeframe
        last_date = self.db_manager.get_last_date(db_name)
        candle = self.get_last_candle(ticker_symbol, timeframe=self.timeframe)
        candle_datetime_naive = candle["Datetime"].replace(tzinfo=None)

        if last_date:
            last_date = last_date.replace(tzinfo=None).date()

        if (candle_datetime_naive - timedelta(minutes=delta)).date() != last_date:
            logger.info("New data inserted for ticker: %s", ticker_symbol)
            ticker = yf.Ticker(ticker_symbol)
            data = ticker.history(period=self.period, interval=timeframe)
            for index, row in data.iloc[:-2].iterrows():
                result = {
                    'Datetime': row.name,
                    'Open': row['Open'],
                    'High': row['High'],
                    'Low': row['Low'],
                    'Close': row['Close'],
                    'Volume': row['Volume']
                }
                self.db_manager.insert_candle(db_name, result)

    def run(self):
        stop_requested = False

        def check_for_stop():
            nonlocal stop_requested
            input("Нажмите Enter для остановки, скрипт остановится при появлении новой свечи...")
            stop_requested = True

        # Запуск потока для ожидания ввода
        stop_thread = threading.Thread(target=check_for_stop)
        stop_thread.start()

        logger.info("Starting PriceParser run method")

        if self.timeframe == '1m':
            waiting_time = 60
        elif self.timeframe == '5m':
            waiting_time = 300
        elif self.timeframe == '30m':
            waiting_time = 1800
        elif self.timeframe == '1h' or self.timeframe == '60m':
            waiting_time = 3600
        else:
            waiting_time = 900

        while not stop_requested:
            for company in self.tickers:
                logger.info("Processing ticker: %s", company)
                db_name = company + '_' + self.timeframe
                candle = self.get_last_candle(company, timeframe=self.timeframe)
                self.db_manager.insert_candle(db_name, candle)
            time.sleep(waiting_time)

        logger.info("Stopping PriceParser")
        stop_thread.join()  # Дожидаемся завершения второстепенного потока


if __name__ == '__main__':
    db_manager = DatabaseManager()
    price_parser = PriceParser(db_manager=db_manager)
    price_parser.run()
