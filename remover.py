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

def remover():
    st.header('Operação de Remoção')
    st.markdown("---")

    opcao = st.radio("Selecione a aba:", ("Filmes", "Diretores", "País"))

    cnx = create_connection()
    cursor = cnx.cursor()

    if opcao == "Filmes":
        # Remoção de filmes
        st.subheader('Remover Filme')
        cursor.execute("SELECT show_id, title FROM filmes")
        filmes = cursor.fetchall()
        options = {f"{show_id} - {title}": show_id for show_id, title in filmes}
        selected_show_id = st.selectbox("Selecione o filme a ser removido", list(options.keys()))

        if st.button("Remover Filme"):
            show_id = options[selected_show_id]
            cursor.execute(f"DELETE FROM filmes WHERE show_id = {show_id}")
            cnx.commit()
            st.success(f"Filme removido com sucesso!")
            st.experimental_rerun()

    elif opcao == "Diretores":
        # Remoção de diretores
        st.subheader('Remover Diretor')
        cursor.execute("SELECT Coddiretores, Nomediretores FROM work_diretores")
        diretores = cursor.fetchall()
        options = {f"{Coddiretores} - {Nomediretores}": Coddiretores for Coddiretores, Nomediretores in diretores}
        selected_director_id = st.selectbox("Selecione o diretor a ser removido", list(options.keys()))

        if st.button("Remover Diretor"):
            director_id = options[selected_director_id]
            cursor.execute(f"DELETE FROM work_diretores WHERE Coddiretores = {director_id}")
            cnx.commit()
            st.success(f"Diretor removido com sucesso!")
            st.experimental_rerun()

    elif opcao == "País":
        # Remoção de País
        st.subheader('Remover País')
        cursor.execute("SELECT pais_id, nome_pais FROM pais_filme")
        paises = cursor.fetchall()
        options = {f"{pais_id} - {nome_pais}": pais_id for pais_id, nome_pais in paises}
        selected_pais_id = st.selectbox("Selecione o país a ser removido", list(options.keys()))

        if st.button("Remover País"):
            id_pais = options[selected_pais_id]
            cursor.execute(f"DELETE FROM pais_filme WHERE pais_id = {id_pais}")
            cnx.commit()
            st.success(f"País removido com sucesso!")
            st.experimental_rerun()

    cursor.close()
    cnx.close()

def main():
    remover()

if __name__ == "_main_":
    main()