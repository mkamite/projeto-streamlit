import streamlit as st


st.header("st.selectbox")
cor = st.selectbox("Selecione uma cor:", 
                   ["vermelho", "azul","verde"],
                   key="sb_cor")
st.write(cor)

st.header("st.multislect")
cores = st.multiselect("Selecione as cores:",
                       ["vermelho", "azul","verde"])

st.write(cores)

st.header("st.radio")
opcao = st.radio("Escolhe uma opção:",
                 ["Audi", "Ferrari", "Chevrolet"],
                 index = 1)
st.write(opcao)




st.header("st.checkbox")
st.markdown("""
# Contrato de trabalho

Nos termos descritos acima, se você marcar como aceito,
poderá realizar o seu cadastro.            
            """)
aceite = st.checkbox("Eu aceito os termos.")
if aceite:
        nome = st.text_input("Digite o seu nome: ")
        idade = st.number_input("Digite sua idade: ")
        data = st.date_input("Data da contratação", format="DD/MM/YYYY")
st.button("Cadastrar")
        
        
st.header("st.Elementos de status")


st.header("Elementos de Status")

botao = st.button("Clique para ver o status")

if botao:
        # st.success("Cadastro realizado com sucesso!", icon="")
        #st.warning("Atenção: evite colocar espaços no nome do usuário")
        #st.info("Esse usuário é Administrador")
        st.success("Cadastro realizado com sucesso")
        st.balloons()
        #st.snow()
        