import streamlit as st
from core.utils import *
from components.widgets.select_if import select_if
from components.tables.indicators import indicators
from components.charts.main_chart import main_chart
from components.charts.nature_all import nature_all
from components.widgets.tabs_children import tabs_childrens


def main():
    if st.button(
        "Voltar a Página Principal",
        help="Clique aqui para voltar a página principal.",
        use_container_width=False,
        type="secondary",
    ):
        st.switch_page("./home.py")
    st.title("Dados brutos")
    st.caption(
        "Tabela de dados financeiros do IFC Campus Araquari, destacando empenhos pagos e a liquidar. Este conjunto de dados é essencial para a análise dos padrões de gastos e para a identificação de áreas prioritárias, auxiliando na gestão e no planejamento orçamentário do campus."
    )
    st.table(st.session_state.df_master)


if __name__ == "__main__":
    st.set_page_config(
        page_title="IF - Análise de Recursos Empenhados e Liquidados",
        page_icon=":chart_with_upwards_trend:",
        layout="wide",
        initial_sidebar_state="collapsed",
    )
    main()
