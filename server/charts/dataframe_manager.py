import pandas as pd
from abc import ABC, abstractmethod
from utils import formatted_months

class DataframeManager(ABC):
    def __init__(self):
        self.df_master = pd.read_csv("./csv/campus_araquari.csv", encoding='ISO-8859-1', sep=";", decimal=",")
    
    @abstractmethod
    def get_datas(self):
        pass

    def get_months(self):
        return formatted_months(self.df_master['mes'].unique())

    def to_float(self):
        try:
            if self.df_master['Empenhado'].apply(lambda x: isinstance(x, str)).any():
                self.df_master['Empenhado'] = self.df_master['Empenhado'].str.replace('.', '').str.replace(',', '.').astype(float)
            if self.df_master['Liquidado'].apply(lambda x: isinstance(x, str)).any():
                self.df_master['Liquidado'] = self.df_master['Liquidado'].str.replace('.', '').str.replace(',', '.').astype(float)
        except Exception as e:
            raise ValueError(f"Error converting columns to numeric: {e}")