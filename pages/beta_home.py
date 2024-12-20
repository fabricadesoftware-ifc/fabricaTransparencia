import streamlit as st
from core.utils import *
from components.widgets.select_if import select_if
from components.tables.indicators import indicators
from components.charts.main_chart import main_chart
from components.charts.nature_all import nature_all
from components.widgets.tabs_children import tabs_childrens


def main():
    st.write("__IFC - Araquari__")
    st.title(":blue[Análise Avançada] de Recursos Empenhados e Liquidados")
    # st.title("Análise de Recursos Empenhados e Liquidados dos :green[Institutos Federais]")
    st.caption(
        "Está é uma versão :red[beta], estamos trabalhando para construir um relatório mais completo. Por favor, nos ajude a melhorar, envie suas sugestões para o email: **teste@gmail.com**."
    )
    st.caption(":blue[Version 1.0.5*]")
    select_if(advanced_report=True)
    indicators()
    main_chart(advanced_report=True)
    nature_all(key="nature_all_1")
    nature_all(advanced_report=True, key="nature_all_2")
    tabs_childrens(advanced_report=True)
    st.divider()
    if st.button(
        "Voltar a Página Principal",
        help="Clique aqui para voltar a página principal.",
        use_container_width=True,
        type="primary",
    ):
        st.switch_page("./home.py")
    if st.button(
        "Ver Dados Brutos",
        help="Clique aqui para ver os dados brutos.",
        use_container_width=True,
    ):
        st.switch_page("pages/dados_brutos.py")


if __name__ == "__main__":
    st.set_page_config(
        page_title="IF - Análise de Recursos Empenhados e Liquidados",
        page_icon=":chart_with_upwards_trend:",
        layout="wide",
        initial_sidebar_state="collapsed",
    )
    main()
