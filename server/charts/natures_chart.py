from . import dataframe_manager

class NaturesChart(dataframe_manager.DataframeManager):
    def __init__(self):
        super().__init__()

    def get_datas(self):
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