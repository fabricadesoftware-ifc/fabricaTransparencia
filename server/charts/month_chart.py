import pandas as pd
from . import dataframe_manager
from utils import formatted_months

class MonthChart(dataframe_manager.DataframeManager):
    def __init__(self):
        super().__init__()

    def formatted_datas_pie(self, data):
        formatted_datas = data.copy()
        formatted_columns = {col: formatted_months(col) for col in formatted_datas.columns}
        formatted_datas = formatted_datas.rename(columns=formatted_columns).applymap(lambda x: 'R$ {:,.2f}'.format(x))

        return formatted_datas
    
    def get_datas(self):
        try:
            self.to_float()
            visible_columns = [
                "Natureza Despesa",
                "mes",
                "Empenhado",
                "Liquidado",
            ]

            df = self.df_master[visible_columns]
            # df_month_values = df[df["mes"].isin(months)] filtro pelo backend
            df_month_values = df
            df_month_values = (
                df_month_values.groupby(["mes", "Natureza Despesa"])[["Empenhado", "Liquidado"]]
                .sum()
                .reset_index()
            )
            df_month_values = df_month_values[["Natureza Despesa", "Empenhado", "Liquidado"]]
            df_month_values = (
                df_month_values.groupby(["Natureza Despesa"])[
                    ["Empenhado", "Liquidado"]
                ]
                .sum()
                .reset_index()
            )
            raw_datas = df_month_values.copy()
            return {
                **raw_datas[["Natureza Despesa", "Empenhado", "Liquidado"]],
                "Filtro": self.get_months()
            }
        except KeyError as e:
            return {"error": f"Missing column: {e}"}
        except AttributeError as e:
            return {"error": f"Dataframe attribute error: {e}"}
        except ValueError as e:
            return {"error": f"Value error: {e}"}
        except Exception as e:
            return {"error": f"An unexpected error occurred: {e}"}
