import streamlit as st
from components.charts.by_month import by_month
from components.charts.by_nature_details import by_nature_details
from components.tables.by_nature_details_month import by_nature_details_month


def tabs_childrens(advanced_report=False):
    tab1, tab2 = st.tabs(["Buscar Por Mês", "Buscar por Natureza"])

    with tab1:
        by_month(advanced_report=advanced_report)
    with tab2:
        by_nature_details(advanced_report=advanced_report)
        by_nature_details_month(advanced_report=advanced_report)
