import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar os dados (use o nome do seu CSV limpo)
df = pd.read_csv("dados_limpos.csv")

st.title("📊 TelecomX - Análise de Churn")
st.write("Projeto de análise de churn em clientes de telecomunicações")

# Mostrar primeiras linhas
st.subheader("Visualização dos dados")
st.dataframe(df.head())

# Gráfico simples de churn
st.subheader("Distribuição da variável Churn")
fig, ax = plt.subplots()
sns.countplot(x="churn", data=df, ax=ax)
st.pyplot(fig)

# Exemplo de filtro interativo
st.subheader("Filtrar por tipo de contrato")
contrato = st.selectbox("Selecione um tipo de contrato", df["Contract"].unique())
st.write(df[df["Contract"] == contrato].head())
