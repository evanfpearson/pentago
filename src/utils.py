import yaml


def read_config(config_path):
    with open(config_path) as f:
        print(yaml.load(f, Loader=yaml.FullLoader))

