impimport pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

st.title("Dashboard SM Vinhos")

# carregar dados
df = pd.read_csv("Mercado Internacional.csv")

st.subheader("Dataset")
st.dataframe(df)

# resumo
st.subheader("Resumo estatístico")
st.write(df.describe())

# gráfico simples
st.subheader("Distribuição dos dados")

coluna = st.selectbox("Escolhe uma coluna", df.columns)

fig, ax = plt.subplots()
df[coluna].value_counts().head(10).plot(kind="bar", ax=ax)

st.pyplot(fig)
