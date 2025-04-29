import streamlit as st
import pandas as pd
from streamlit_echarts import st_echarts
from core.utils import *
from core.dataframe_manager import DataframeManager


def by_year(advanced_report=False):
    df_manager = DataframeManager()
    available_years = df_manager.get_years()

    if "selected_years" not in st.session_state:
        st.session_state.selected_years = []

    st.session_state.selected_years = st.multiselect(
        "Selecione o Ano",
        options=available_years,
        default=st.session_state.selected_years,
        key=f"indicators_year_{advanced_report}",
        placeholder="Selecione o Ano",
    )

    if not st.session_state.selected_years:
        st.info("Selecione um ano", icon="🔎")
    else:
        raw_datas = []
        for y in st.session_state.selected_years:
            df = df_manager.get_df_by_all_nature(y)
            raw_datas.append(df[1])

        if len(raw_datas) > 0:
            raw_datas_df = pd.concat(raw_datas)
        else:
            raw_datas_df = pd.DataFrame()

        if not raw_datas_df.empty and "Natureza Despesa" in raw_datas_df.columns:
            summed_df = raw_datas_df.groupby(["Natureza Despesa"]).sum().reset_index()
        else:
            summed_df = pd.DataFrame()

        st.table(summed_df)

        row2 = st.columns(2, gap="medium")

        with row2[0]:
            st.caption("## Empenhado (Anual)")
            st.caption(
                f"Recurso empenhado pela Direção do IFC - Araquari em {', '.join(map(str, st.session_state.selected_years))}"
            )
            empenhado_chart = get_options_year_detail(summed_df, "Empenhado (R$)")
            st_echarts(options=empenhado_chart, height="500px")

        with row2[1]:
            st.caption("## Liquidado (Anual)")
            st.caption(
                f"Empenho liquidado pela Direção do IFC - Araquari em {', '.join(map(str, st.session_state.selected_years))}"
            )
            liquidado_chart = get_options_year_detail(summed_df, "Liquidado (R$)")
            st_echarts(options=liquidado_chart, height="500px")
