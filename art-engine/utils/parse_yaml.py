""" Helper function that reads in the YAML config file """

import yaml

from pathlib import Path


def read_yaml() -> object:
    config_path = Path.cwd() / 'art-engine' / 'config.yaml'

    with config_path.open() as file:
        config_data = yaml.safe_load(file)

    return config_data
