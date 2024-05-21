import streamlit as st
import pandas as pd
from streamlit_echarts import st_echarts
from utils import *
from classes.dataframe_manager import DataframeManager

def by_month(onlyTable=False):
    df_manager = DataframeManager()  

    st.caption("## Empenhado")
    st.caption('Recurso empenhado pela Direção do IFC - Araquari')
    [raw_datas, formatted_datas] = df_manager.get_df_month_detail(value='Empenhado')
    if onlyTable:
        st.table(formatted_datas)
    else:
        chart_options = get_options_month(raw_datas)
        st_echarts(chart_options, height="500px", key="df_moth_empenho")

    st.caption("## Liquidado")
    st.caption('Empenhos liquidados pela Direção do IFC - Araquari')
    [raw_datas, formatted_datas] = df_manager.get_df_month_detail(value='Liquidado')
    if onlyTable:
        st.table(formatted_datas)
    else:
        chart_options = get_options_month(raw_datas)
        st_echarts(chart_options, height="500px", key="df_moth_liquidado")