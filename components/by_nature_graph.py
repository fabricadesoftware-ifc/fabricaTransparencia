import streamlit as st
import pandas as pd
from streamlit_echarts import st_echarts
from utils import *
from classes.dataframe_manager import DataframeManager


def by_nature_graph(onlyTable=False):
    df_manager = DataframeManager()
    months = [formatted_months(month) for month in st.session_state.df_master["Mês"].unique()]
    st.session_state.months = st.multiselect(
        label="Selecione o mês",
        key=f"get_month_{onlyTable}_{id}",
        options=months,
        placeholder="Selecione o mês",
    )
    if st.session_state.months == None:
        st.info("Selecione um mês", icon="ℹ️")

    else:
        row2 = st.columns(2, gap="medium")
        with row2[0]:
            st.caption("## Empenhado")
            st.caption("Recurso empenhado pela Direção do IFC - Araquari")
            meses = [unformatted_months(month) for month in st.session_state.months]
            raw_datas = df_manager.get_df_month_monetary_values(meses, "Empenhado")
            chart_options = get_options_month_detail(raw_datas, "Empenhado")
            st_echarts(chart_options, height="500px", key=f"{st.session_state}df_moth_detail_comitted")

        with row2[1]:
            st.caption("## Liquidado")
            st.caption("Empenho liquidado pela Direção do IFC - Araquari")
            meses = [unformatted_months(month) for month in st.session_state.months]
            print(meses)
            raw_datas = df_manager.get_df_month_monetary_values(meses, "Liquidado")
            print(raw_datas)
            chart_options = get_options_month_detail(raw_datas, "Liquidado")
            print(chart_options)
            st_echarts(chart_options, height="500px", key=f"{st.session_state}df_moth_detail_liquidated")
