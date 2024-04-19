import streamlit as st
import pandas as pd
import altair as alt
import matplotlib.pyplot as plt
import numpy as np


def run():
    st.set_page_config(
        page_title="Empenhos IFC Araquari | Empenhos Pagos",
        page_icon="📃",
        layout="wide",
        initial_sidebar_state="expanded",
        menu_items={
            "Get Help": "https://www.extremelycoolapp.com/help",
            "Report a bug": "https://www.extremelycoolapp.com/bug",
            "About": """
                Este projeto de pesquisa tem como objetivo apresentar dados financeiros sobre o IFC Campus Araquari, no que respeita aos empenhos pagos e à liquidar..
                \\
                \\
                Professor Responsavel: [Fábio Longo de Moura](www.github.com/ldmfabio) 
                \\
                Aluno Responsavel: [Mateus Lopes Albano](www.github.com/mateus-lopes)
                \
                \

            """,
        },
    )
    st.markdown(
        """
        ## 📃 Empenhos IFC Araquari | Empenhos Pagos
        #####
        """
    )

    df = pd.read_csv("./assets/csv/pagos.csv", sep=";", decimal=",")
    colunas_visiveis = [
        "Natureza Despesa",
        "Natureza Despesa Detalhada",
        "Nome Favorecido",
        "Mês",
        "Saldo",
    ]
    filtered_df = df[colunas_visiveis]

    tab1, tab2 = st.tabs(["Dados", "Gráficos"])

    with tab1:
        st.write(filtered_df)

    with tab2:

        tab3, tab4, tab5 = st.tabs(
            ["Por Mês", "Por Natureza de Despesa", "Por Mês e Natureza de Despesa"]
        )

        with tab3:
            df_grouped = filtered_df.groupby("Mês").sum().reset_index()

            chart = (
                alt.Chart(df_grouped)
                .mark_bar()
                .encode(x="Mês", y="Saldo", color="Mês")
                .properties(width=800, height=400)
            )

            st.altair_chart(chart, use_container_width=True)

        with tab4:

            def filtro_dados(filtered, mes):
                if mes == "Todos":
                    return filtered
                return filtered[filtered["Mês"] == mes]

            def barras_agrupadas():
                meses = filtered_df["Mês"]
                naturezas = filtered_df["Natureza Despesa"]
                saldos = filtered_df["Saldo"]
                df = pd.DataFrame(
                    {"Mês": meses, "Natureza Despesa": naturezas, "Saldo": saldos}
                )

                meses_unicoss = ["Todos"] + df["Mês"].unique().tolist()
                mes_selecionadoo = st.selectbox("Selecione mês", meses_unicoss)

                df_final = filtro_dados(df, mes_selecionadoo)
                grouped_df = (
                    df_final.groupby(["Mês", "Natureza Despesa"]).sum().reset_index()
                )

                fig, ax = plt.subplots()
                meses = grouped_df["Mês"].unique()
                largura_barra = 0.35
                indice = np.arange(len(meses))

                for i, mes in enumerate(meses):
                    df_mes = grouped_df[grouped_df["Mês"] == mes]
                    for j, categoria in enumerate(df_mes["Natureza Despesa"].unique()):
                        valores = df_mes[df_mes["Natureza Despesa"] == categoria][
                            "Saldo"
                        ].values
                        ax.bar(
                            indice[i] + largura_barra * j,
                            valores,
                            largura_barra,
                            label=categoria,
                        )
                        ax.text(
                            indice[i] + largura_barra * j,
                            valores[0] + 50,
                            str(f"{valores[0]:.2f}"),
                            ha="center",
                            va="bottom",
                            rotation=0,
                        )

                ax.set_xlabel("Natureza Despesa Detalhada por Mês")
                ax.set_ylabel("Saldo")
                ax.set_title("")
                # ax.set_xticks(indice + largura_barra / 2)
                ax.legend(
                    title="Natureza Despesa", bbox_to_anchor=(1.05, 1), loc="upper left"
                )
                return fig

            st.pyplot(barras_agrupadas())

        with tab5:

            def filtrar_dados(filtered_df, mes, natureza):
                if mes == "Todos" and natureza == "Todas":
                    return filtered_df
                elif mes == "Todos":
                    return filtered_df[filtered_df["Natureza Despesa"] == natureza]
                elif natureza == "Todas":
                    return filtered_df[filtered_df["Mês"] == mes]
                else:
                    return filtered_df[
                        (filtered_df["Mês"] == mes)
                        & (filtered_df["Natureza Despesa"] == natureza)
                    ]

            meses_unicos = ["Todos"] + filtered_df["Mês"].unique().tolist()
            naturezas_unicas = ["Todas"] + filtered_df[
                "Natureza Despesa"
            ].unique().tolist()

            mes_selecionado = st.selectbox("Selecione o mês", meses_unicos)
            natureza_selecionada = st.selectbox(
                "Selecione a natureza de despesa", naturezas_unicas
            )

            df_filtrado = filtrar_dados(
                filtered_df, mes_selecionado, natureza_selecionada
            )

            df_grouped = (
                df_filtrado.groupby(["Mês", "Natureza Despesa"]).sum().reset_index()
            )

            chart2 = (
                alt.Chart(df_grouped)
                .mark_bar()
                .encode(
                    x="Mês",
                    y="Saldo",
                    color="Natureza Despesa",
                    tooltip=[
                        "Mês",
                        "Natureza Despesa",
                        alt.Tooltip("Saldo", title="Saldo"),
                    ],
                )
                .properties(width=800, height=400)
                .interactive()
            )

            st.altair_chart(chart2, use_container_width=True)


if __name__ == "__main__":
    run()
