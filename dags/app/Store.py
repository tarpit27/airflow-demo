from datetime import datetime
from pandas import DataFrame
import os


class Store:
    def __init__(self, df: DataFrame, file_name):
        self.df = df
        self.file_name = file_name

    def store_df(self):
        output_location = os.getcwd() + '/data/updated/'
        if not os.path.exists(output_location):
            os.mkdir(output_location)
        self.df.to_csv(output_location + self.file_name + '_' + str(datetime.now()) , index=False)
        print("Dataframe stored")