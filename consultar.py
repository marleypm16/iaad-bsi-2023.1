import mysql.connector
import streamlit as st
import pandas as pd

def create_connection():
    # Substitua as informações abaixo pelas suas credenciais do banco de dados
    cnx = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234",
        database="estante_de_filmes"
    )
    return cnx

def consultar():
    st.header("Consulta do Banco de Dados")
    st.markdown("---")

    # Conectar-se ao banco de dados
    cnx = create_connection()
    cursor = cnx.cursor()

    # Seleção de abas
    tab_selected = st.radio("Selecione a Tabela:", ("Filmes", "Diretores", "Países"))

    if tab_selected == "Filmes":
        # Consultar e exibir os dados da tabela "filmes"
        st.subheader("Tabela Filmes")
        query_filmes = "SELECT * FROM filmes"
        df_filmes = pd.read_sql_query(query_filmes, cnx)
        st.dataframe(df_filmes)
    elif tab_selected == "Diretores":
        # Consultar e exibir os dados da tabela "work_diretores"
        st.subheader("Tabela Diretores")
        query_diretores = "SELECT * FROM work_diretores"
        df_diretores = pd.read_sql_query(query_diretores, cnx)
        st.dataframe(df_diretores)
    elif tab_selected == "Países":
        # Consultar e exibir os dados da tabela "pais_filme"
        st.subheader("Tabela Países")
        query_pais = "SELECT * FROM pais_filme"
        df_paises = pd.read_sql_query(query_pais, cnx)
        st.dataframe(df_paises)

    # Descrição da estrutura das tabelas
    if tab_selected == "Diretores":
        st.subheader("Descrição da Tabela Diretores")
        query_descricao = "DESCRIBE work_diretores"
        df_descricao = pd.read_sql_query(query_descricao, cnx)
        st.dataframe(df_descricao)

    # Listar todos os bancos de dados
    cursor.execute("SHOW DATABASES")
    databases = cursor.fetchall()
    st.subheader("Bancos de Dados Disponíveis")
    for database in databases:
        st.write(database[0])

    # Fechar a conexão com o banco de dados
    cursor.close()
    cnx.close()

def main():
    consultar()

if _name_ == "main":
    main()