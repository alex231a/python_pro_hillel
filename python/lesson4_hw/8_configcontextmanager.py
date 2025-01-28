# Напишіть власний контекстний менеджер для роботи з файлом конфігурацій (
# формат .ini або .json). Менеджер має автоматично зчитувати конфігурацію
# при вході в контекст і записувати зміни в файл після завершення роботи.

import json
import os

class ConfigContextManager:
    """Context manager for working with config files"""

    def __init__(self, config_file:str):
        self.config_file = config_file
        self.config = None

    def __enter__(self):
        """Read config file and seve information in self.config"""
        try:
            if os.path.getsize(self.config_file) == 0:
                self.config = {}
            else:
                with open(self.config_file, 'r') as f:
                    self.config = json.load(f)
        except json.JSONDecodeError:
            print(
                f"Error while reading from {self.config_file}.")
            self.config = {}
        return self.config

    def __exit__(self, exc_type, exc_val, exc_tb):
        """write to config file"""
        with open(self.config_file, 'w') as f:
            json.dump(self.config, f)


if __name__ == '__main__':
    with ConfigContextManager('config.json') as config:
        config['database'] = {
            "host": "localhost123",
            "port": 5431,
            "user": "admin_user",
            "password": "secret_user1"
        }
        config['debug'] = True
