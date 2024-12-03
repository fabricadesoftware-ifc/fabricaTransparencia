import streamlit as st

def select_if(advanced_report=False):
    if advanced_report:
        st.write(
            """
            Este projeto tem por objetivo possibilitar à comunidade o acompanhamento da execução do orçamento do campus.
            As informações são apresentadas considerando, ao longo do tempo, os valores de Despesas Empenhadas e Despesas Liquidadas.
            """
        )
    else:
        st.write(
            """
            Este projeto tem por objetivo possibilitar à comunidade o acompanhamento da execução do orçamento do campus.
            As informações são apresentadas considerando, ao longo do tempo, os valores de Despesas Empenhadas e Despesas Liquidadas.
            """
        )
        layout_cols = st.columns((1, 1, 2))

        with layout_cols[0]:
            state_option = st.selectbox(
                f"Selecione o Estado",
                ["SC", "..."],
            )

        with layout_cols[1]:
            campus_option = st.selectbox(
                f"Selecione o Campus",
                ["Araquari", "..."],
            )
    
    st.markdown('''<div style="color: #888; font-size: .8em;position: absolute; right: 0; bottom: -2em;">
        Professor Responsavel: <a href="www.github.com/ldmfabio" style="padding-right: 1em">Fábio Longo de Moura</a> 
        Aluno Responsavel: <a href="www.github.com/mateus-lopes">Mateus Lopes Albano</a>
    </div>''', unsafe_allow_html=True)