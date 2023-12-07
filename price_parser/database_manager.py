from pymongo import MongoClient
import pandas as pd
from datetime import timedelta
import os


class DatabaseManager:
    def __init__(self, db_name='historical_prices'):
        # Получение данных из переменных окружения
        host = os.environ.get('host')  # Значение по умолчанию - 'localhost'
        port = os.environ.get('port')  # Значение по умолчанию - 27017

        # Преобразование порта в int, если он представлен строкой
        port = int(port) if isinstance(port, str) and port.isdigit() else port

        self.client = MongoClient(host, port)
        self.db = self.client[db_name]

    def insert_candle(self, collection_name, candle_data):
        """Добавление одной свечи в нужную коллекцию"""
        collection = self.db[collection_name]
        collection.insert_one(candle_data)

    def insert_many_candles(self, collection_name, candle_data):
        """Добавление нескльких свечей за раз"""
        collection = self.db[collection_name]
        collection.insert_many(candle_data)

    def get_last_date(self, collection_name):
        """Получение последней свечи в коллекции"""
        collection = self.db[collection_name]
        try:
            last_record = next(collection.find().sort('Datetime', -1).limit(1))
            return last_record['Datetime']
        except StopIteration:
            return None

    def export_to_csv(self, days=5, output_file='output.csv'):
        """Выгрузка данных для обучения"""
        print(f'available collections: {self.get_collection_names()}')
        chosen_collection = str(input("write chosen collection: "))
        if chosen_collection not in self.get_collection_names():
            print('Wrong value for collection')
            self.export_to_csv(days=days, output_file=output_file)

        collection = self.db[chosen_collection]
        last_date = self.get_last_date(chosen_collection)
        last_date = last_date.replace(tzinfo=None)
        start_date = last_date - timedelta(days=days)
        query = {
            'Datetime': {'$gte': start_date}
        }

        data = list(collection.find(query))
        if data:
            df = pd.DataFrame(data)
            df['Datetime'] = pd.to_datetime(df['Datetime'])
            # Удаление столбца '_id', так как он не нужен для CSV
            df.drop(columns=['_id'], inplace=True)

            # Экспорт DataFrame в CSV
            df.to_csv(output_file, index=False)
            print(f"Data exported to {output_file}")
        else:
            print("No data found for the specified period.")

    def save_dataframe_to_collection(self, df, collection_name):
        """
        Сохраняет DataFrame в указанную коллекцию MongoDB. Если коллекция сущестует,
        то просто дозаписываем новые данные. Метод для добавления сгенерированных признаков.

        Args:
            df (pandas.DataFrame): DataFrame для сохранения.
            collection_name (str): Название коллекции для сохранения данных.
        """
        if not isinstance(df, pd.DataFrame):
            print("Предоставленный объект не является DataFrame.")
            return

        collection = self.db[collection_name]
        # Преобразование DataFrame в список словарей
        records = df.to_dict('records')

        # Вставка данных в коллекцию
        collection.insert_many(records)
        print(f"DataFrame сохранен в коллекцию {collection_name}.")

    def get_collection_names(self):
        """Возвращает список доступных коллекций"""
        collections = self.db.list_collection_names()
        return collections

    def close_connection(self):
        self.client.close()
