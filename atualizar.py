import streamlit as st
import mysql.connector

def create_connection():
    # Substitua as informações abaixo pelas suas credenciais do banco de dados
    cnx = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234",
        database="estante_de_filmes"
    )
    return cnx

def update_filme(show_id, title, duration, listen_in, coddiretores):
    cnx = create_connection()
    cursor = cnx.cursor()
    
    try:
        update_query = "UPDATE filmes SET title = %s, duration = %s, listen_in = %s, Coddiretores = %s WHERE show_id = %s"
        cursor.execute(update_query, (title, duration, listen_in, coddiretores, show_id))
        
        cnx.commit()
        st.success("Filme atualizado com sucesso!")
        
    except mysql.connector.Error as err:
        st.error(f"Erro ao atualizar filme: {err}")
        cnx.rollback()
    
    finally:
        cursor.close()
        cnx.close()

def update_pais(pais_id, nome_pais, show_id):
    cnx = create_connection()
    cursor = cnx.cursor()
    
    try:
        update_query = "UPDATE pais_filme SET show_id = %s, nome_pais = %s WHERE pais_id = %s"
        cursor.execute(update_query, (show_id, nome_pais, pais_id))
        
        cnx.commit()
        st.success("País do filme atualizado com sucesso!")
        
    except mysql.connector.Error as err:
        st.error(f"Erro ao atualizar país do filme: {err}")
        cnx.rollback()
    
    finally:
        cursor.close()
        cnx.close()

def atualizar():
    st.title("Atualizar Dados")

    opcao = st.radio("Selecione o que deseja atualizar:", ["Filme", "País do Filme"])

    if opcao == "Filme":
        st.subheader("Cadastrar Filme")
        show_id = st.selectbox("Selecione o ID do Filme:", options=get_existing_movie_ids())
        title = st.text_input("Título do Filme:")
        duration = st.text_input("Duração do Filme:")
        listen_in = st.text_input("Gênero do Filme:")
        coddiretores = st.number_input("ID do Diretor:", min_value=1, step=1)

        if st.button("Atualizar Filme"):
            update_filme(show_id, title, duration, listen_in, coddiretores)

    elif opcao == "País do Filme":
        st.subheader("Atualizar País do Filme")
        pais_id = st.selectbox("Selecione o ID do País:", options=get_existing_country_ids())
        nome_pais = st.text_input("Nome do País:")
        show_id = st.number_input("ID do Filme:", min_value=1, step=1)

        if st.button("Atualizar País do Filme"):
            update_pais(pais_id, nome_pais, show_id)

def get_existing_movie_ids():
    cnx = create_connection()
    cursor = cnx.cursor()
    cursor.execute("SELECT show_id FROM filmes")
    existing_ids = [result[0] for result in cursor.fetchall()]
    cursor.close()
    cnx.close()
    return existing_ids

def get_existing_country_ids():
    cnx = create_connection()
    cursor = cnx.cursor()
    cursor.execute("SELECT pais_id FROM pais_filme")
    existing_ids = [result[0] for result in cursor.fetchall()]
    cursor.close()
    cnx.close()
    return existing_ids

if __name__== "_main_":
    atualizar()