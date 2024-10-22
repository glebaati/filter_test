import json


class ConfigReader:
    with open("config.json", 'r') as f:
        config = json.load(f)

    @classmethod
    def __getitem__(cls, item):
        return cls.config[item]
