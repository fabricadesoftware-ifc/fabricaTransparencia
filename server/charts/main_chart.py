from utils import formatted_month
from . import dataframe_manager

class MainChart(dataframe_manager.DataframeManager):
    def __init__(self):
        super().__init__()

    def get_datas(self):
        self.to_float()
        visible_columns = [
            'mes',  
            'Empenhado',
            'Liquidado',
        ]

        df_main = self.df_master[visible_columns].groupby(['mes'])[['Empenhado', 'Liquidado']].sum().reset_index()
        df_main["Empenhado (R$)"] = df_main["Empenhado"].map("R$ {:,.2f}".format)
        df_main["Liquidado (R$)"] = df_main["Liquidado"].map("R$ {:,.2f}".format)
        df_main['mes'] = df_main['mes'].map(lambda x: formatted_month(x))

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