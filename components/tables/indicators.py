import streamlit as st
from core.dataframe_manager import DataframeManager


def indicators():
    df_manager = DataframeManager()
    st.divider()
    st.caption("### Indicadores Gerais")

    year = st.selectbox(
        "Selecione o Ano",
        options=df_manager.get_years(),
        index=0,
        key="indicators_year",
    )

    [committed, settled, balance] = df_manager.get_indicators(year)
    row = st.columns(3)

    with row[0]:
        st.markdown(
            f"<p style='font-size: 2.4em; font-weight: 700;'>{committed}</p>",
            unsafe_allow_html=True,
        )
        st.caption("*Montante Empenhado*")

    with row[1]:
        st.markdown(
            f"<p style='font-size: 2.4em; font-weight: 700;'>{settled}</p>",
            unsafe_allow_html=True,
        )
        st.caption("*Montante Liquidado*")

    with row[2]:
        st.markdown(
            f"<p style='font-size: 2.4em; font-weight: 700; color: red;'>{balance}</p>",
            unsafe_allow_html=True,
        )
        st.caption("*Montante Pendente de Liquidação*")
