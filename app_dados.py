import streamlit as st
import pandas as pd

@st.cache_data
def carregar_dados():
    dados = pd.read_csv("acidentes.csv")
    return dados

dados = carregar_dados()

#tabela_dados = st.dataframe(dados)
tabela_dados = st.data_editor(dados)
salvar  = carregar = st.button("Salvar dados")

if salvar:
    tabela_dados.to_csv("dados_alterados.csv",index=False)
    st.success("Dados alterados e gravados com sucesso!")

mostrar_grafico = st.toggle("Mostrar gráfico")

if mostrar_grafico:
    contagem_municipio = dados["municipio"].value_counts()
    #st.dataframe(contagem_municipio)
    st.bar_chart(contagem_municipio)
    #st.line_chart(contagem_municipio)