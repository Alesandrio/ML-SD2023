import pandas as pd
import tools

class DataPreparation:

    def __init__(self, iteration, directory) -> None:
        self.iteration = iteration
        self.directory = directory
        self.test_size = tools.read_yaml('./config/config.yaml')['test_size']
        

    def clear_data(self, train, test):
        train = train.dropna()
        test = test.dropna()
        return train, test

    def split_data(self, train, test, iteration, directory, test_size) -> None:
        return tools.save_dataset(X = train, y = test, iteration = iteration, dir = directory, test_size = test_size)    