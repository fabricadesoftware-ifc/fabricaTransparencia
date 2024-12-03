import streamlit as st
import pandas as pd
from core.utils import *
from core.dataframe_manager import DataframeManager
from streamlit_echarts import st_echarts

def by_nature_details(advanced_report=False):
    df_manager = DataframeManager()
    nature = [item for item in st.session_state.df_master["Natureza Despesa"].unique()]
    st.session_state.nature = st.selectbox(
        label="Selecione a Natureza da Despesa", 
        options=nature, 
        key=f'{advanced_report}select_nature', 
        index=None,
        placeholder="Selecione a Natureza da Despesa"
    )
    if st.session_state.nature == None:
        st.info("Nenhuma Natureza Despesa selecionada", icon="ℹ️")
    else:
        option2, option3, df_by_nature_test_1, df_by_nature_test_2, df_by_nature_test_3 = df_manager.get_df_by_nature(st.session_state.nature)
        st_echarts(options=option2, height="600px")
        st.table(df_by_nature_test_2)
