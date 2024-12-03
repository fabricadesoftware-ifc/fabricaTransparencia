import streamlit as st
from core.dataframe_manager import DataframeManager
from streamlit_echarts import st_echarts

def by_nature_details_month(advanced_report=False):
    df_manager = DataframeManager()
    type = st.selectbox(
        label="Selecione o Tipo de Despesa", 
        options=["Empenhado", "Liquidado"], 
        key=f'{advanced_report}select_nature_type', 
        index=0,
        placeholder="Selecione o Tipo de Despesa"
    )
    if st.session_state.nature == None:
        st.info("Nenhuma Natureza Despesa selecionada", icon="ℹ️")
    else:
        option2, option3, df_by_nature_test_1, df_by_nature_test_2, df_by_nature_test_3 = df_manager.get_df_by_nature(st.session_state.nature, type)    
        
        if type == None:
            st.info("Nenhuma Natureza Despesa selecionada", icon="ℹ️")
        else:
            st_echarts(options=option3, height="600px")
