import streamlit as st
import pandas as pd
from streamlit_echarts import st_echarts
from core.utils import *
from core.dataframe_manager import DataframeManager

def by_nature(onlyTable=False):
    df_manager = DataframeManager()  
    months = [formatted_months(month) for month in st.session_state.df_master['Mês'].unique()]
    st.session_state.month = st.multiselect(
        label="Selecione o mês",
        key=f'get_month321_{onlyTable}',
        options=months,
        placeholder="Selecione o mês",
    )
    if st.session_state.month == None:
        st.info("Selecione um mês", icon="ℹ️")

    if not st.session_state.month == None:
        st.caption("## Empenhado x Liquidado")
        st.caption('Visualização por Mês')

        raw_datas = []

        unformatted_months_list = [unformatted_months(month) for month in st.session_state.month]
        df = df_manager.get_df_month_values(unformatted_months_list)
        raw_datas.append(df)

        if len(raw_datas) > 0:
            raw_datas_df = pd.concat(raw_datas)
        else:
            raw_datas_df = []

        st.table(raw_datas_df)
