from st_aggrid import AgGrid
import pandas as pd
import streamlit as st
from utils import *
from components.select_if import select_if
from components.tabs_container import tabs_container

def main():    
    st.title("Análise de Recursos Empenhados e Liquidados dos :green[Institutos Federais]")
    select_if()
    tabs_container()

if __name__ == "__main__":
    st.set_page_config(
        page_title="IF - Análise de Recursos Empenhados e Liquidados", 
        page_icon=":chart_with_upwards_trend:",
        layout="wide",
    )
    main()
