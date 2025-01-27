import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")

st.title("Personal finance dashboard")

df = pd.read_csv("finances.csv")
df["Month"] = df["Date"].apply(lambda x: "-".join(x.split("-")[:-1]))
df["Date"] = pd.to_datetime(df["Date"])
df["Date"] = df["Date"].apply(lambda x: x.date())
df = df[df["Category"] != "Income"]
del df["Appears On Your Statement As"], df["Reference"]


def filter_data(df, month, selected_categories):
    df_filtered = df[df["Month"] == month]
    if selected_categories:
        df_filtered = df_filtered[df_filtered["Category"].isin(selected_categories)]
    return df_filtered

month = st.sidebar.selectbox("Month", df["Month"].unique())
categories = df["Category"].unique().tolist()
selected_categories = st.sidebar.multiselect("Filter by category",
                                             categories, default=categories)

df_filtered = filter_data(df, month, selected_categories)

c1, c2 = st.columns([0.6, 0.4])
c1.dataframe(df_filtered)

category_distribution = df_filtered.groupby("Category")["Amount"].sum().reset_index()
fig = px.pie(category_distribution, values='Amount', names='Category',
             title='Distribution by category', hole=0.3)

c2.plotly_chart(fig, use_container_width=True)