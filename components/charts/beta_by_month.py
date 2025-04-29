import streamlit as st
import pandas as pd
from streamlit_echarts import st_echarts
from core.utils import *
from core.dataframe_manager import DataframeManager
from components.charts.by_month import by_month


def by_month2(onlyTable=False):
    df_manager = DataframeManager()
    typeChart = st.selectbox(
        "Selecione o tipo do gráfico",
        ["Empenhado", "Liquidado"],
        key=f"typeChart{onlyTable}",
        index=0,
        placeholder="Selecione o tipo do gráfico",
    )
    if typeChart == "Empenhado":
        [raw_datas, formatted_datas] = df_manager.get_df_month_detail(value="Empenhado")
        if onlyTable:
            chart_options = get_options_month(raw_datas)
            st_echarts(chart_options, height="500px", key=f"df_moth_empenho{onlyTable}")
            st.table(formatted_datas)
        else:
            chart_options = get_options_month(raw_datas)
            st_echarts(chart_options, height="500px", key=f"df_moth_empenho{onlyTable}")
    else:
        [raw_datas, formatted_datas] = df_manager.get_df_month_detail(value="Liquidado")
        if onlyTable:
            chart_options = get_options_month(raw_datas)
            st_echarts(
                chart_options, height="500px", key=f"df_moth_liquidado{onlyTable}"
            )
            st.table(formatted_datas)
        else:
            chart_options = get_options_month(raw_datas)
            st_echarts(
                chart_options, height="500px", key=f"df_moth_liquidado{onlyTable}"
            )
