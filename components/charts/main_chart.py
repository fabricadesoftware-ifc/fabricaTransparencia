import streamlit as st
from streamlit_echarts import st_echarts
from core.dataframe_manager import DataframeManager
from core.utils import brazilian_currency

def main_chart(advanced_report=False):
    df_manager = DataframeManager()
    [options, df] = df_manager.get_options_main()
    settled = st.session_state.df_master['Liquidado'].sum()
    committed = st.session_state.df_master['Empenhado'].sum() - settled

    if advanced_report:
        st.table(df)
    else:
        st.caption("#")
        st.caption("### Total de Recursos Empenhados e Liquidados")
        options = {
            **options,
            "grid": {"left": "1%", "right": "25%", "bottom": "3%", "containLabel": True},
            "series": [
                *options['series'],
                {
                    "name": "Soma Total (R$)",
                    "type": "pie",
                    "radius": '60%',
                    "center": ["90%", "50%"],
                    "data": [
                        {"value": settled, "name": "Liquidado"},
                        {"value": committed, "name": "Empenhado"},
                    ],
                    "emphasis": {
                        "label": {
                            "show": True,
                        }
                    },
                    "label": {
                        "show": False,
                        "formatter": "{d}%",
                        "fontSize": 15,
                        "fontWeight": "bold",
                        "position": 'center'
                    }
                }
            ],
        }
        st_echarts(options=options, height="400px")