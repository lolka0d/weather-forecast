import streamlit as st
import plotly.express as px
import pandas as pd


st.title("TITLE")
x_name = st.selectbox("SELECT THE DATA FIELD (x):", ("GDP", "Happiness"))
y_name = st.selectbox("SELECT THE DATA FIELD (y):", ("GDP", "Happiness"))


def get_data(x, y):
    df = pd.read_csv("happy.csv")
    x_res = df[x].to_list()
    y_res = df[y].to_list()

    return x_res, y_res


x_result, y_result = get_data(x_name.lower(), y_name.lower())

figure = px.scatter(x=x_result, y=y_result, labels={"x": x_name, "y": y_name})

st.plotly_chart(figure)
