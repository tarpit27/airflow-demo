import pandas as pd
import os


class Load:
    def __init__(self, file_path):
        self.file_path = file_path

    def load_file(self):
        return pd.read_csv(os.getcwd() + '/data/' + self.file_path)
