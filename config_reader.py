import json

class ConfigReader:
    def __init__(self):
        with open(r"config.json", 'r') as file:
            self.config = json.load(file)

    def get_timeout(self):
        return self.config.get("timeout")
    def get_url(self):
        return self.config.get("URL")