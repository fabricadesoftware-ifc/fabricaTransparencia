import streamlit as st
from core.utils import get_campi
from core.dataframe_manager import DataframeManager


def select_if(advanced_report=False):
    df_manager = DataframeManager()

    if advanced_report:
        st.write(
            """
            Este projeto tem por objetivo possibilitar à comunidade o acompanhamento da execução do orçamento dos campi.
            As informações são apresentadas considerando, ao longo do tempo, os valores de Despesas Empenhadas e Despesas Liquidadas.
            """
        )
        year_option = "2024"
        if "year" not in st.session_state:
            st.session_state.year = year_option

        campus_option = "Araquari"
        if "campus" not in st.session_state:
            st.session_state.campus = campus_option

    else:
        st.write(
            """
            Este projeto tem por objetivo possibilitar à comunidade o acompanhamento da execução do orçamento dos campi.
            As informações são apresentadas considerando, ao longo do tempo, os valores de Despesas Empenhadas e Despesas Liquidadas.
            """
        )
        layout_cols = st.columns((1, 1, 3))

        campi = get_campi("./assets/data/")

        with layout_cols[0]:
            campus_option = st.selectbox(
                f"Selecione o Campus",
                campi,
                index=(
                    campi.index(st.session_state.get("campus", campi[0]))
                    if "campus" in st.session_state
                    and st.session_state["campus"] in campi
                    else 0
                ),
            )
            st.session_state.campus = campus_option.lower().replace(" ", "_")

        anos = df_manager.get_years()

        with layout_cols[1]:
            year_option = st.selectbox(
                f"Selecione o Ano",
                anos,
            )
            st.session_state.year = year_option

        with layout_cols[2]:
            ...

    st.markdown(
        """<div style="color: #888; font-size: .8em;position: absolute; right: 0; bottom: -2em;">
        Professor Responsável: <a href="www.github.com/ldmfabio" style="padding-right: 1em">Fábio Longo de Moura</a> 
        Alunos Responsáveis: <a href="www.github.com/mateus-lopes">Mateus L. Albano</a>, <a href="www.github.com/gabriel04alves">Gabriel Alves</a>, <a href="www.github.com/mariaeduardanichelle">Maria Eduarda N. Ferreira</a>,  
    </div>""",
        unsafe_allow_html=True,
    )

    return year_option
