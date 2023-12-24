import pandas as pd
from sklearn.model_selection import train_test_split
import os
import yaml

#returns splitted data if split=True or full clean dataset if split=False
def preprocessing(data_path: str, checkEmpty = False):

    data = pd.read_csv(data_path)

    for col in data.columns:
        if type(data[col].iloc[0]) is str:
            data = data.drop([col], axis=1)

    if checkEmpty:
        data = data.dropna()
        print('Your data has been checked and cleared of empty values!')
    
    return data

def save_dataset(X, y, iteration = 0, test_size = 0.33, dir = None):
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = test_size)

    if dir:

        if not os.path.exists(os.path.join(dir, str(iteration))):
            os.mkdir(os.path.join(dir, str(iteration)))

        X_train.to_csv(dir + f'/{iteration}/X_train.csv', index=False)
        print('X_train: ' + dir + f'/{iteration}/X_train.csv')
        X_test.to_csv(dir + f'/{iteration}/X_test.csv', index=False)
        print('X_test: ' + dir + f'/{iteration}/X_test.csv')
        y_train.to_csv(dir + f'/{iteration}/y_train.csv', index=False)
        print('y_train: ' + dir + f'/{iteration}/y_train.csv')
        y_test.to_csv(dir + f'/{iteration}/y_test.csv', index=False)
        print('y_test: ' + dir + f'/{iteration}/y_test.csv')
        print('Your data is completely saved')
        return X_train, X_test, y_train, y_test
    
    else:
        print('There is no directory to save dataset!')

def mean_squared_error(x, y):

    initial_length = len(x)
    res = 0
    for i in range(initial_length):
        res += (y[i] - x[i])**2
    
    return res/initial_length

def union_datasets(datasets = None, path = None):
    data = pd.read_csv(datasets[0])
    for x in datasets[1:]:
        data = pd.concat([data, pd.read_csv(x)]).reset_index().drop(['index'], axis = 1)
    data.to_csv(path)

def read_yaml(path_to_yaml: str):
    with open(path_to_yaml, 'r') as file:
        parsed_yaml = yaml.safe_load(file)
    return parsed_yaml