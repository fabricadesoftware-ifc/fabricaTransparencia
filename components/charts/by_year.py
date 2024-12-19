import streamlit as st
import pandas as pd
from streamlit_echarts import st_echarts
from core.utils import *
from core.dataframe_manager import DataframeManager

def by_year(advanced_report=False):
    df_manager = DataframeManager()

    year = st.multiselect(
        "Selecione o Ano",
        options=df_manager.get_years(),
        default=[df_manager.get_years()[0]],
        key=f"indicators_year_{advanced_report}",
    )

    if not year:
        st.info("Selecione um ano", icon="ℹ️")
    else:
        raw_datas = []
        for y in year:
            df = df_manager.get_df_by_all_nature(y)
            raw_datas.append(df[1]) 

        if len(raw_datas) > 0:
            raw_datas_df = pd.concat(raw_datas)
        else:
            raw_datas_df = []

        if not raw_datas_df.empty and 'Natureza Despesa' in raw_datas_df.columns:
            summed_df = raw_datas_df.groupby(['Natureza Despesa']).sum().reset_index()
        else:
            summed_df = pd.DataFrame()

        st.table(summed_df)

        row2 = st.columns(2, gap="medium")
        
        with row2[0]:
            st.caption("## Empenhado (Anual)")
            st.caption(f"Recurso empenhado pela Direção do IFC - Araquari em {', '.join(map(str, year))}")
            

        with row2[1]:
            st.caption("## Liquidado (Anual)")
            st.caption(f"Empenho liquidado pela Direção do IFC - Araquari em {', '.join(map(str, year))}")
            
