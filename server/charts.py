import matplotlib.pyplot as plt
import pandas as pd
from utils import formatted_months

class DataframeManager:
    def __init__(self):
        self.df_master = pd.read_csv("./csv/campus_araquari.csv", encoding='ISO-8859-1', sep=";", decimal=",")

    def set_new_datas(self, new_df):
        self.df_master = new_df
    
    def get_global_indicators(self):      
        self.to_float()
        committed_formatted = "{:,.2f}".format(self.df_master['Empenhado'].sum())
        settled_formatted = "{:,.2f}".format(self.df_master['Liquidado'].sum())
        balance_formatted = "{:,.2f}".format(self.df_master['Empenhado'].sum() - self.df_master['Liquidado'].sum())

        return {
            "committed": committed_formatted,
            "settled": settled_formatted,
            "balance": balance_formatted,
        }
    
    def main_chart(self):
        self.to_float()
        visible_columns = [
            'mes',
            'Empenhado',
            'Liquidado',
        ]
        print(self.df_master.columns)

        # Verificar se as colunas necessárias estão presentes no DataFrame
        missing_columns = [col for col in visible_columns if col not in self.df_master.columns]
        if missing_columns:
            raise KeyError(f"Colunas ausentes no DataFrame: {missing_columns}")

        df_main = self.df_master[visible_columns].groupby(['mes'])[['Empenhado', 'Liquidado']].sum().reset_index()
        df_main["Empenhado (R$)"] = df_main["Empenhado"].map("R$ {:,.2f}".format)
        df_main["Liquidado (R$)"] = df_main["Liquidado"].map("R$ {:,.2f}".format)
        df_main['mes'] = df_main['mes'].map(lambda x: formatted_months(x))

        total_empenhado = "R$ {:,.2f}".format(self.df_master['Empenhado'].sum())
        total_liquidado = "R$ {:,.2f}".format(self.df_master['Liquidado'].sum())

        df_main.loc[len(df_main)] = ['Total', total_empenhado, total_liquidado, total_empenhado, total_liquidado]

        return {
            "line1": df_main['Empenhado'].tolist()[0:-1],
            "line2": df_main['Liquidado'].tolist()[0:-1],
            "pie": [self.df_master['Empenhado'].sum(), self.df_master['Liquidado'].sum()],
            "dataframe": [{
                "month": df_main['mes'].tolist()[i],
                "committed": df_main['Empenhado (R$)'].tolist()[i], 
                "liquidated": df_main['Liquidado (R$)'].tolist()[i]
            } for i in range(len(df_main))],
        }
    
    def all_natures_chart(self):
        self.to_float()
        visible_columns = [
            'Natureza Despesa',
            'Empenhado',
            'Liquidado',
        ]

        all_nature = self.df_master['Natureza Despesa'].unique().tolist()
        df = self.df_master[visible_columns]
        df_by_all_nature = df[df['Natureza Despesa'].isin(all_nature)]
        df_by_all_nature = df_by_all_nature.groupby(['Natureza Despesa'])[['Empenhado', 'Liquidado']].sum().reset_index()

        option = {
            "bar1": df_by_all_nature['Empenhado'].tolist(),
            "bar2": df_by_all_nature['Liquidado'].tolist(),
            "yAxis": df_by_all_nature['Natureza Despesa'].tolist(),
        }

        df_by_all_nature['Empenhado (R$)'] = df_by_all_nature['Empenhado'].map('R$ {:,.2f}'.format)
        df_by_all_nature['Liquidado (R$)'] = df_by_all_nature['Liquidado'].map('R$ {:,.2f}'.format)
        
        total_empenhado = "R$ {:,.2f}".format(df_by_all_nature['Empenhado'].sum())
        total_liquidado = "R$ {:,.2f}".format(df_by_all_nature['Liquidado'].sum())
        df_by_all_nature.loc[len(df_by_all_nature)] = ['Total', total_empenhado, total_liquidado, total_empenhado, total_liquidado]

        return {
            **option,
            "dataframe": [{
                "nature": df_by_all_nature['Natureza Despesa'].tolist()[i],
                "committed": df_by_all_nature['Empenhado (R$)'].tolist()[i], 
                "liquidated": df_by_all_nature['Liquidado (R$)'].tolist()[i]
            } for i in range(len(df_by_all_nature))],
        }
    
    def get_months(self):
        print(self.df_master['mes'].unique())
        return ['ola', 'ola2']

    def to_float(self):
        if self.df_master['Empenhado'].apply(lambda x: isinstance(x, str)).any():
            self.df_master['Empenhado'] = self.df_master['Empenhado'].str.replace('.', '').str.replace(',', '.').astype(float)
        if self.df_master['Liquidado'].apply(lambda x: isinstance(x, str)).any():
            self.df_master['Liquidado'] = self.df_master['Liquidado'].str.replace('.', '').str.replace(',', '.').astype(float)