from train import Train
from datapreparation import DataPreparation
from dataload import LoadData
from tools import read_yaml

if __name__ == '__main__':

    config = read_yaml('./config/config.yaml')

    client = LoadData()
    client.connect()
    data_prepatation = DataPreparation()

    train = dataset.train
    test = dataset.test

    train, test = data_prepatation.clear_data(train, test)

    X_train, X_test, y_train, y_test = data_prepatation.split_data(
        train=train, 
        test=test, 
        test_size = config['test_size'],
        dir = './datasets',
        iteration=1
        )
    
    model = Train.train(X_train, y_train)
    Train.save_model(model, '.models/')

    client.disconnect()