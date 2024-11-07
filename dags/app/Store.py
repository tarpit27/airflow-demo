from datetime import datetime
from pandas import DataFrame
import os


class Store:
    def __init__(self, df: DataFrame, file_name):
        self.df = df
        self.file_name = file_name

    def store_df(self):
        print(type(self.df))
        self.df.to_csv(os.getcwd() + '/data/updated/' + self.file_name + '_' + str(datetime.now()) , index=False)
        print("Dataframe stored")