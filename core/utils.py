import pandas as pd
import altair as alt
import streamlit as st
import uuid
import random
from babel.numbers import format_currency


def get_options_month_detail(df, tipo):
    series = []
    if tipo == "Empenhado":
        data = [
            {
                "value": df.loc[
                    df["Natureza Despesa"] == natureza_despesa, "Empenhado"
                ].values[0],
                "name": natureza_despesa,
            }
            for natureza_despesa in df["Natureza Despesa"].unique()
        ]
    elif tipo == "Liquidado":
        data = [
            {
                "value": df.loc[
                    df["Natureza Despesa"] == natureza_despesa, "Liquidado"
                ].values[0],
                "name": natureza_despesa,
            }
            for natureza_despesa in df["Natureza Despesa"].unique()
        ]
    else:
        data = []

    series.append(
        {
            "type": "pie",
            "id": str(uuid.uuid4()),
            "radius": "50%",
            "center": ["50%", "70%"],
            "label": {"formatter": "{d}% | R$ {@[tipo]}"},
            "encode": {
                "itemName": "Natureza Despesa",
                "value": "Empenhado",
                "tooltip": "Empenhado",
            },
            "data": data,
        }
    )

    return {
        "legend": {"left": "1%", "right": "2%"},
        "tooltip": {"trigger": "axis", "showContent": False},
        "series": series,
    }


def unformatted_months(month):
    dict = {
        "Janeiro": "01/2024",
        "Fevereiro": "02/2024",
        "Março": "03/2024",
        "Abril": "04/2024",
        "Maio": "05/2024",
        "Junho": "06/2024",
        "Julho": "07/2024",
        "Agosto": "08/2024",
        "Setembro": "09/2024",
        "Outubro": "10/2024",
        "Novembro": "11/2024",
        "Dezembro": "12/2024",
    }

    return dict[month]


def formatted_months(month):
    dict = {
        "01/2024": "Janeiro",
        "02/2024": "Fevereiro",
        "03/2024": "Março",
        "04/2024": "Abril",
        "05/2024": "Maio",
        "06/2024": "Junho",
        "07/2024": "Julho",
        "08/2024": "Agosto",
        "09/2024": "Setembro",
        "10/2024": "Outubro",
        "11/2024": "Novembro",
        "12/2024": "Dezembro",
    }

    return dict[month]


def brazilian_currency(money):
    return format_currency(money, "BRL", locale="pt_BR")


def get_options_month(df):
    df.columns = [
        formatted_months(col) if col != "Natureza Despesa" else col
        for col in df.columns
    ]  # Renaming columns to formatted months
    source = [df.columns.tolist()]
    for i in range(df.shape[0]):
        source.append(df.iloc[i].tolist())

    series = []
    for i in range(len(source)):
        series.append(
            {
                "type": "line",
                "smooth": True,
                "seriesLayoutBy": "row",
                "emphasis": {"focus": "series"},
            }
        )

    return {
        "tooltip": {"trigger": "axis"},
        "legend": {"top": "2%", "left": "1%", "right": "2%"},
        "dataset": {"source": source},
        "xAxis": {
            "type": "category",
            "boundaryGap": False,
            "axisLabel": {"margin": 20},
        },
        "yAxis": {"gridIndex": 0},
        "grid": {
            "top": "20%",
            "left": "1%",
            "right": "2%",
            "bottom": "0%",
            "containLabel": True,
        },
        "series": series,
    }


def clean_convert_column(df, column_name):
    # Replace thousand separators with decimals (assuming '.' is decimal separator)
    df[column_name] = df[column_name].str.replace(",", ".")

    # Handle potential decimal separators other than '.' (e.g., ',')
    df[column_name] = df[column_name].str.replace(r"[^\d\-+\.]", "", regex=True)

    # Try converting to float, replacing errors with NaN (or a specified value)
    df[column_name] = pd.to_numeric(df[column_name], errors="coerce")

    return df


def create_simple_chart():
    df = pd.DataFrame({"x": [1, 2, 3, 4, 5], "y": [10, 20, 30, 40, 50]})

    chart = alt.Chart(df).mark_line(point=True).encode(x="x", y="y")

    return chart


def get_campus_option():
    id = random.randint(1, 1000)
    campus_option = st.selectbox(
        f"Selecione o Campus {id}",
        ["Araquari", "Camboriú", "Sombrio", "Videira"],
    )

    return campus_option


def create_card(
    title="Titulo do Grafico",
    desciption="pequena descrição sobre o grafico",
    border=False,
    onlyTable=False,
):
    container_col = st.container(border=border)
    container_col.write(f"### {title}")
    container_col.caption(f"{desciption}")

    if onlyTable:
        st.write("dataframe vem aqui")
    else:
        layout_cols = st.columns((1, 1, 2))

        with layout_cols[0]:
            option1 = get_campus_option()

        with layout_cols[1]:
            option2 = get_campus_option()


def create_card_table(
    title="Titulo do Grafico",
    desciption="pequena descrição sobre o grafico",
    border=False,
):
    container_col = st.container(border=border)
    container_col.write(f"### {title}")
    container_col.caption(f"{desciption}")
    layout_cols = st.columns((1, 1, 2))

    with layout_cols[0]:
        option1 = get_campus_option()

    with layout_cols[1]:
        option2 = get_campus_option()

    st.write("dataframe vem aqui")


def main_table():
    df = pd.read_csv(
        "../assets/data/xls/empenhos.csv", encoding="utf-8", sep=";", decimal=","
    )

    colunas_visiveis = [
        "Natureza Despesa",
        "Natureza Despesa Detalhada",
        "Métrica",
        "Mês",
        "Empenhado",
        "Liquidado",
    ]

    df = df[colunas_visiveis]
    df["Empenhado"] = (
        df["Empenhado"].str.replace(".", "").str.replace(",", ".").astype(float)
    )
    df["Liquidado"] = (
        df["Liquidado"].str.replace(".", "").str.replace(",", ".").astype(float)
    )
    df["Empenhado Formatado"] = df["Empenhado"].map("R$ {:,.2f}".format)
    df["Liquidado Formatado"] = df["Liquidado"].map("R$ {:,.2f}".format)

    df_mes = df.groupby(["Mês"])[["Empenhado", "Liquidado"]].sum().reset_index()
    df_mes["Empenhado Formatado"] = df_mes["Empenhado"].map("R$ {:,.2f}".format)
    df_mes["Liquidado Formatado"] = df_mes["Liquidado"].map("R$ {:,.2f}".format)

    return df_mes
