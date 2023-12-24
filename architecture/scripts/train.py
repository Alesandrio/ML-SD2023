import config


class Train:
    def __init__(self, model_params_path) -> None:
        parser = config.ConfigParser(model_params_path)
        cfg = parser.parse()
        self.params = cfg

    def feature_extraction(self) -> None:
        pass

    def train(self, X_train, y_train) -> None:
        print('Learning is started...')

    def save_model(self, model, path_to_save):
        print('Saving model...')
        print(f'Model is saved: {path_to_save}')

    def fit_predict(self):
        pass

    def inference(self):
        pass