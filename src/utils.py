import yaml


def read_config(config_path) -> dict:
    with open(config_path) as f:
        return yaml.load(f, Loader=yaml.FullLoader)


class MoveError(Exception):
    def __init__(self, message):
        self.message = message
