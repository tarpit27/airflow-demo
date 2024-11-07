import pandas as pd
from pandas import DataFrame

class Transform:

    def __init__(self, df: DataFrame):
        self.df = df

    def transform_df(self):
        print("Transforming DataFrame")

        self.df.dropna(how='all', axis='columns', inplace=True)

        print("Transformed dataframe: ", self.df.to_string())

        return self.df