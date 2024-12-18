import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st
from streamlit.logger import get_logger
from core.utils import *

LOGGER = get_logger(__name__)


class DataframeManager:
    def __init__(self):
        self.init_session_state()

    def init_session_state(self):
        if "error_message" not in st.session_state:
            st.session_state.error_message = ""
        if "df_master" not in st.session_state:
            st.session_state.df_master = pd.read_csv(
                "assets/data/xls/empenhos.csv",
                encoding="utf-8",
                sep=";",
                decimal=",",
            )
        if "month" not in st.session_state:
            st.session_state.month = "01"
        if "year" not in st.session_state:
            st.session_state.year = "2024"

    def get_df_month_values(self, months):
        self.to_float()
        visible_columns = [
            "Natureza Despesa",
            "Mês",
            "Empenhado",
            "Liquidado",
        ]

        df = st.session_state.df_master[visible_columns]
        if isinstance(months, str):
            months = [months]

        df_month_values = df[df["Mês"].isin(months)]
        visible_columns = [
            "Natureza Despesa",
            "Empenhado",
            "Liquidado",
        ]
        df_month_values = df_month_values[visible_columns]
        df_month_values = (
            df_month_values.groupby(["Natureza Despesa"])[["Empenhado", "Liquidado"]]
            .sum()
            .reset_index()
        )
        total_empenhado = df_month_values["Empenhado"].sum()
        total_liquidado = df_month_values["Liquidado"].sum()
        df_total = pd.DataFrame(
            {
                "Natureza Despesa": ["Total"],
                "Empenhado": [total_empenhado],
                "Liquidado": [total_liquidado],
            }
        )
        df_month_values = pd.concat([df_month_values, df_total])
        df_month_values["Empenhado"] = df_month_values["Empenhado"].map(
            "R$ {:,.2f}".format
        )
        df_month_values["Liquidado"] = df_month_values["Liquidado"].map(
            "R$ {:,.2f}".format
        )

        return df_month_values

    def get_df_month_monetary_values(self, months, tipo):
        self.to_float()
        visible_columns = [
            "Natureza Despesa",
            "Mês",
            "Empenhado",
            "Liquidado",
        ]

        df = st.session_state.df_master[visible_columns]
        df_month_values = df[df["Mês"].isin(months)]
        df_month_values = (
            df_month_values.groupby(["Mês", "Natureza Despesa"])[
                ["Empenhado", "Liquidado"]
            ]
            .sum()
            .reset_index()
        )
        visible_columns = [
            "Natureza Despesa",
            "Empenhado",
            "Liquidado",
        ]
        df_month_values = df_month_values[visible_columns]
        df_month_values = (
            df_month_values.groupby(["Natureza Despesa"])[["Empenhado", "Liquidado"]]
            .sum()
            .reset_index()
        )
        raw_datas = df_month_values.copy()

        visible_columns = ["Natureza Despesa", tipo]
        raw_datas = raw_datas[visible_columns]
        return raw_datas

    def get_df_month_detail(self, value="Empenhado"):
        self.to_float()
        visible_columns = [
            "Natureza Despesa",
            "Mês",
            "Empenhado",
            "Liquidado",
        ]

        df = st.session_state.df_master[visible_columns]
        df_month_detail = (
            df.groupby(["Mês", "Natureza Despesa"])[["Empenhado", "Liquidado"]]
            .sum()
            .reset_index()
        )
        df_month_detail["Empenhado (R$)"] = st.session_state.df_master["Empenhado"].map(
            "R$ {:,.2f}".format
        )
        df_month_detail["Liquidado (R$)"] = st.session_state.df_master["Liquidado"].map(
            "R$ {:,.2f}".format
        )
        pivoted = pd.pivot_table(
            df_month_detail, values=value, index="Natureza Despesa", columns="Mês"
        )
        pivoted = pivoted.fillna(0)
        raw_datas = pivoted.reset_index()

        formatted_datas = pivoted.copy()
        formatted_columns = {
            col: formatted_months(col) for col in formatted_datas.columns
        }
        formatted_datas = formatted_datas.rename(columns=formatted_columns).applymap(
            lambda x: "R$ {:,.2f}".format(x)
        )

        return [raw_datas, formatted_datas]

    def get_options_main(self):
        self.to_float()
        visible_columns = [
            "Mês",
            "Empenhado",
            "Liquidado",
        ]

        df = st.session_state.df_master[visible_columns]
        df_main = df.groupby(["Mês"])[["Empenhado", "Liquidado"]].sum().reset_index()
        df_main["Empenhado (R$)"] = df_main["Empenhado"].map("R$ {:,.2f}".format)
        df_main["Liquidado (R$)"] = df_main["Liquidado"].map("R$ {:,.2f}".format)
        df_main["Mês"] = df_main["Mês"].map(lambda x: formatted_months(x))

        total_empenhado = "R$ {:,.2f}".format(df["Empenhado"].sum())
        total_liquidado = "R$ {:,.2f}".format(df["Liquidado"].sum())
        df_main.loc[len(df_main)] = [
            "Total",
            total_empenhado,
            total_liquidado,
            total_empenhado,
            total_liquidado,
        ]

        return [
            {
                "title": {"text": ""},
                "tooltip": {"trigger": "axis"},
                "legend": {"data": ["Liquidado", "Empenhado"], "left": "1%"},
                "grid": {
                    "left": "1%",
                    "right": "2%",
                    "bottom": "3%",
                    "containLabel": True,
                },
                "toolbox": {"feature": {"saveAsImage": {}}},
                "xAxis": {
                    "type": "category",
                    "boundaryGap": False,
                    "axisLabel": {"margin": 20},
                    "data": df_main["Mês"].tolist(),
                },
                "yAxis": {"type": "value"},
                "series": [
                    {
                        "name": "Liquidado",
                        "type": "line",
                        "stack": "Liquidado",
                        "smooth": True,
                        "data": df_main["Liquidado"].tolist(),
                    },
                    {
                        "name": "Empenhado",
                        "type": "line",
                        "stack": "Empenhado",
                        "smooth": True,
                        "data": df_main["Empenhado"].tolist(),
                    },
                ],
            },
            df_main[["Mês", "Empenhado (R$)", "Liquidado (R$)"]],
        ]

    def get_df_by_all_nature(self):
        self.to_float()
        visible_columns = [
            "Natureza Despesa",
            "Empenhado",
            "Liquidado",
        ]

        all_nature = st.session_state.df_master["Natureza Despesa"].unique().tolist()
        df = st.session_state.df_master[visible_columns]
        df_by_all_nature = df[df["Natureza Despesa"].isin(all_nature)]
        df_by_all_nature = (
            df_by_all_nature.groupby(["Natureza Despesa"])[["Empenhado", "Liquidado"]]
            .sum()
            .reset_index()
        )

        option2 = {
            "yAxis": {
                "type": "category",
                "data": df_by_all_nature["Natureza Despesa"].tolist(),
            },
            "series": [
                {
                    "name": "Empenhado",
                    "type": "bar",
                    "emphasis": {"focus": "series"},
                    "data": df_by_all_nature["Empenhado"].tolist(),
                },
                {
                    "name": "Liquidado",
                    "type": "bar",
                    "emphasis": {"focus": "series"},
                    "data": df_by_all_nature["Liquidado"].tolist(),
                },
            ],
        }

        df_by_all_nature["Empenhado (R$)"] = df_by_all_nature["Empenhado"]
        df_by_all_nature["Liquidado (R$)"] = df_by_all_nature["Liquidado"]

        total_empenhado = df_by_all_nature["Empenhado"].sum()
        total_liquidado = df_by_all_nature["Liquidado"].sum()
        df_by_all_nature.loc[len(df_by_all_nature)] = [
            "Total",
            total_empenhado,
            total_liquidado,
            total_empenhado,
            total_liquidado,
        ]

        return [
            option2,
            df_by_all_nature[["Natureza Despesa", "Empenhado (R$)", "Liquidado (R$)"]],
        ]

    def get_df_by_nature(self, nature, type_value="Empenhado"):
        self.to_float()
        visible_columns = [
            "Natureza Despesa",
            "Empenhado",
            "Liquidado",
        ]
        if isinstance(nature, str):
            nature = [nature]

        df = st.session_state.df_master[visible_columns]
        df_by_nature_test_1 = df[df["Natureza Despesa"].isin(nature)]
        df_by_nature_test_1 = (
            df_by_nature_test_1.groupby(["Natureza Despesa"])[
                ["Empenhado", "Liquidado"]
            ]
            .sum()
            .reset_index()
        )

        visible_columns = [
            "Natureza Despesa",
            "Natureza Despesa Detalhada",
            "Empenhado",
            "Liquidado",
        ]
        df = st.session_state.df_master[visible_columns]
        df_by_nature_test_2 = df[df["Natureza Despesa"].isin(nature)]
        df_by_nature_test_2 = (
            df_by_nature_test_2.groupby(["Natureza Despesa Detalhada"])[
                ["Empenhado", "Liquidado"]
            ]
            .sum()
            .reset_index()
        )

        df = st.session_state.df_master[
            [
                "Natureza Despesa",
                "Natureza Despesa Detalhada",
                "Métrica",
                "Empenhado",
                "Liquidado",
            ]
        ]
        df_by_nature_test_3 = df[df["Natureza Despesa"].isin(nature)].reset_index()
        df_by_nature_test_3 = df_by_nature_test_3[
            ["Natureza Despesa Detalhada", "Métrica", "Empenhado", "Liquidado"]
        ]

        option2 = {
            "title": {
                "text": "Natureza Despesa Detalhada x Natureza Despesa",
                "left": "center",
            },
            "tooltip": {"trigger": "axis", "axisPointer": {"type": "shadow"}},
            "legend": {
                "data": ["Empenhado", "Liquidado"],
                "top": "8%",
                "left": "center",
            },
            "grid": {
                "right": "3%",
                "left": "3%",
                "bottom": "3%",
                "top": "45%",
                "containLabel": True,
            },
            "xAxis": {"type": "value"},
            "yAxis": {
                "type": "category",
                "data": df_by_nature_test_2["Natureza Despesa Detalhada"].tolist(),
            },
            "series": [
                {
                    "name": "Empenhado",
                    "type": "bar",
                    "data": df_by_nature_test_2["Empenhado"].tolist(),
                    "barWidth": "35%",
                },
                {
                    "name": "Liquidado",
                    "type": "bar",
                    "data": df_by_nature_test_2["Liquidado"].tolist(),
                    "barWidth": "35%",
                },
                {
                    "name": "Example Data",
                    "type": "pie",
                    "radius": ["12%", "25%"],
                    "data": [
                        {
                            "value": df_by_nature_test_1["Empenhado"].sum(),
                            "name": "Empenhado",
                        },
                        {
                            "value": df_by_nature_test_1["Liquidado"].sum(),
                            "name": "Liquidado",
                        },
                    ],
                    "center": ["50%", "28%"],
                    "emphasis": {
                        "label": {"show": True, "fontSize": 13, "fontWeight": "bold"}
                    },
                    "label": {"show": False, "position": "center", "formatter": "{d}%"},
                },
            ],
        }

        option3 = {
            "title": {"text": "Natureza Despesa Detalhada x Mês", "left": "center"},
            "tooltip": {"trigger": "axis"},
            "xAxis": {"type": "value"},
            "yAxis": {
                "type": "category",
                "data": df_by_nature_test_3["Métrica"].unique().tolist(),
            },
            "grid": {
                "left": "3%",
                "right": "3%",
                "bottom": "3%",
                "top": "30%",
                "containLabel": True,
            },
            "series": [],
        }

        for natureza in (
            df_by_nature_test_3["Natureza Despesa Detalhada"].unique().tolist()
        ):
            data = df_by_nature_test_3[
                df_by_nature_test_3["Natureza Despesa Detalhada"] == natureza
            ][type_value].tolist()
            series = {
                "name": natureza,
                "type": "bar",  # Changed to bar
                "data": data,
                "emphasis": {"focus": "series"},
            }
            option3["series"].append(series)

        legend = {
            "data": df_by_nature_test_3["Natureza Despesa Detalhada"].unique().tolist(),
            "top": "10%",
            "left": "left",
        }

        option3["legend"] = legend

        return [
            option2,
            option3,
            df_by_nature_test_1,
            df_by_nature_test_2,
            df_by_nature_test_3,
        ]

    def get_years(self):
        return st.session_state.df_master["Mês"].str[-4:].unique().tolist()

    def get_indicators(self, year="2024"):
        self.to_float()
        df = st.session_state.df_master[
            st.session_state.df_master["Mês"].str.endswith(year)
        ]
        committed = df["Empenhado"].sum()
        settled = df["Liquidado"].sum()
        balance = committed - settled
        committed_formatted = brazilian_currency(committed)
        settled_formatted = brazilian_currency(settled)
        balance_formatted = brazilian_currency(balance)

        return [committed_formatted, settled_formatted, balance_formatted]

    def clean_df(self):
        pass

    def to_float(self):
        if (
            st.session_state.df_master["Empenhado"]
            .apply(lambda x: isinstance(x, str))
            .any()
        ):
            st.session_state.df_master["Empenhado"] = (
                st.session_state.df_master["Empenhado"]
                .str.replace(".", "")
                .str.replace(",", ".")
                .astype(float)
            )
        if (
            st.session_state.df_master["Liquidado"]
            .apply(lambda x: isinstance(x, str))
            .any()
        ):
            st.session_state.df_master["Liquidado"] = (
                st.session_state.df_master["Liquidado"]
                .str.replace(".", "")
                .str.replace(",", ".")
                .astype(float)
            )
