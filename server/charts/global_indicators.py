from . import dataframe_manager

class GlobalIndicators(dataframe_manager.DataframeManager):
    def __init__(self):
        super().__init__()

    def get_datas(self):
        try:
            self.to_float()
            committed = self.df_master['Empenhado'].sum()
            settled = self.df_master['Liquidado'].sum()
            balance = committed - settled
            
            committed_formatted = "{:,.2f}".format(committed)
            settled_formatted = "{:,.2f}".format(settled)
            balance_formatted = "{:,.2f}".format(balance)

            return {
                "committed": committed_formatted,
                "settled": settled_formatted,
                "balance": balance_formatted,
            }
        except KeyError as e:
            return {"error": f"Missing column: {e}"}
        except AttributeError as e:
            return {"error": f"Dataframe attribute error: {e}"}
        except Exception as e:
            return {"error": f"An unexpected error occurred: {e}"}
