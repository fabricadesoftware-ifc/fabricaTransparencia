import streamlit as st
from utils import *
from components.by_month import by_month
from components.by_nature import by_nature
from components.by_nature_graph import by_nature_graph
from components.by_nature_details import by_nature_details

def tabs_childrens(onlyTable=False):
    tab1, tab2, tab3 = st.tabs(['Por Mês', 'Por Natureza', 'Por Natureza Detalhada'])

    with tab1:
        by_month(onlyTable=onlyTable)
    with tab2:
        if (onlyTable):
            by_nature(onlyTable=onlyTable)
        else:
            by_nature_graph(onlyTable=onlyTable)
    with tab3:
        by_nature_details(onlyTable=onlyTable)
