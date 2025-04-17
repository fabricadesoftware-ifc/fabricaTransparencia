import streamlit as st
from core.utils import get_campi


def select_if(advanced_report=False):
    if advanced_report:
        st.write(
            """
            Este projeto tem por objetivo possibilitar à comunidade o acompanhamento da execução do orçamento do campus.
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
            Este projeto tem por objetivo possibilitar à comunidade o acompanhamento da execução do orçamento do campus.
            As informações são apresentadas considerando, ao longo do tempo, os valores de Despesas Empenhadas e Despesas Liquidadas.
            """
        )
        layout_cols = st.columns((1, 1, 1, 3))

        with layout_cols[0]:
            state_option = st.selectbox(
                f"Selecione o Estado",
                ["SC", "..."],
            )

        campi = get_campi("./assets/data/xls")

        with layout_cols[1]:
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

        with layout_cols[2]:
            year_option = st.selectbox(
                f"Selecione o Ano",
                ["2024", "2025", "..."],
            )
            st.session_state.year = year_option

        with layout_cols[3]:
            ...

    st.markdown(
        """<div style="color: #888; font-size: .8em;position: absolute; right: 0; bottom: -2em;">
        Professor Responsavel: <a href="www.github.com/ldmfabio" style="padding-right: 1em">Fábio Longo de Moura</a> 
        Aluno Responsavel: <a href="www.github.com/mateus-lopes">Mateus Lopes Albano</a>
    </div>""",
        unsafe_allow_html=True,
    )

    return year_option
