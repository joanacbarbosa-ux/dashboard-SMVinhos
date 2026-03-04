import pandas as pd
import streamlit as st

st.title("Dashboard SM Vinhos")

# carregar dataset
df = pd.read_csv("Mercado Internacional.csv")

st.subheader("Dados")
st.dataframe(df)

st.subheader("Resumo estatístico")
st.write(df.describe())

st.subheader("Colunas do dataset")
st.write(df.columns)
