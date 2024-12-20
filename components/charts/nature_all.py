import streamlit as st
from core.dataframe_manager import DataframeManager
from streamlit_echarts import st_echarts

def nature_all(advanced_report=False, key="nature_all"):
    df_manager = DataframeManager()

    year = st.selectbox(
        "Selecione o Ano",
        options=df_manager.get_years(),
        index=0,
        key=f"{key}_year",
    )

    [option, get_dataframe_by_nature] = df_manager.get_df_by_all_nature(year)

    options = {
        **option,
        "title": {
            "text": '',
        },
        "tooltip": {
            "trigger": 'axis',
            "axisPointer": {
                "type": 'shadow'
            },
        },
        "legend": {
            "data": ['Empenhado', 'Liquidado'],
            "left": '0%',
            "top": '1%',
        },
        "grid": {
            "left": '3%',
            "right": '4%',
            "bottom": '3%',
            "top": '8%',
            "containLabel": True
        },
        "xAxis": {
            "type": 'value',
            "boundaryGap": [0, 0.01]
        }
    }

    if advanced_report:
        st.table(get_dataframe_by_nature)
    else:
        st.caption("##")
        st.caption("### Total de Recursos Empenhados e Liquidados por Natureza de Despesa")
        st_echarts(options=options, height="500px", key=f'{advanced_report}_nature_chart')

