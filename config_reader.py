import json


class ConfigReader:
    with open("config.json", 'r') as f:
        config = json.load(f)

    @staticmethod
    def get_value(item):
        return ConfigReader.config.get(item)
