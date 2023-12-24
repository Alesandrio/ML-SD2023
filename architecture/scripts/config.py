import argparse
import yaml

class ConfigParser:

    def __init__(self, path_to_yaml_config) -> None:
        self.path = path_to_yaml_config

    def parse(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('--model_config', default=self.path)
        args = parser.parse_args()

        with open(args.model_config) as f:
            cfg = yaml.load(f, Loader=yaml.FullLoader)

        return cfg