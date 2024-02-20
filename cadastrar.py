import mysql.connector
import streamlit as st

def create_connection():
    # Substitua as informações abaixo pelas suas credenciais do banco de dados
    cnx = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234",
        database="estante_de_filmes"
    )
    return cnx

def cadastrar():
    st.header("Operação de Cadastro")
    st.markdown("---")
    opcao = st.radio("Selecione a aba:", ("Filmes", "Diretores", "País"))


    cnx = create_connection()
    cursor = cnx.cursor()

    # Cadastrar Filmes
    if opcao == 'Filmes':

        st.subheader("Cadastrar Filmes")

        cursor.execute("SELECT Coddiretores, Nomediretores FROM work_diretores")
        resultado = cursor.fetchall()
        valores_diretores = {str(row[0]): row[1] for row in resultado}

        with st.form(key="include_filme"):
            input_title = st.text_input(label="Insira o Título do Filme", max_chars=40)
            input_duration = st.text_input(label="Insira a Duração do Filme", max_chars=25)
            input_listen_in = st.text_input(label="Insira os Gêneros do Filme", max_chars=500)
            input_Coddiretor = st.selectbox(label="Selecione o Diretor", options=list(valores_diretores.keys()))
            input_button_submit = st.form_submit_button('Cadastrar')

        if input_button_submit:
            if len(input_title) != 0:
                query = "INSERT INTO filmes (title, duration, listen_in, Coddiretores) VALUES (%s, %s, %s, %s)"
                values = (input_title, input_duration, input_listen_in, input_Coddiretor)
                cursor.execute(query, values)
                cnx.commit()

                st.success("Filme adicionado com sucesso!")
                st.info(f'Título do Filme: {input_title}')
                st.info(f'Duração: {input_duration}')
                st.info(f'Gêneros: {input_listen_in}')
                st.info(f'Código do Diretor: {input_Coddiretor}')

                st.warning('Atualizando página')
                st.experimental_rerun()

            elif len(input_title) == 0:
                st.warning('Você deve inserir o Título do Filme')
    if opcao == 'Diretores':

        # Cadastrar Diretores
        st.subheader("Cadastrar Diretores")

        with st.form(key="include_diretor"):
            input_Nomediretores = st.text_input(label="Insira o Nome do Diretor", max_chars=255)
            input_tipo_show = st.selectbox(label="Selecione o Tipo de Show", options=["Movie", "TV Show"])
            input_button_submit = st.form_submit_button('Cadastrar')

        if input_button_submit:
            if len(input_Nomediretores) != 0:
                query = "INSERT INTO work_diretores (Nomediretores, tipo_show) VALUES (%s, %s)"
                values = (input_Nomediretores, input_tipo_show)
                cursor.execute(query, values)
                cnx.commit()

                st.success("Diretor adicionado com sucesso!")
                st.info(f'Nome do Diretor: {input_Nomediretores}')
                st.info(f'Tipo de Show: {input_tipo_show}')

                st.warning('Atualizando página')
                st.experimental_rerun()

            elif len(input_Nomediretores) == 0:
                st.warning('Você deve inserir o Nome do Diretor')
    
    if opcao == 'País':
        st.subheader("Cadastrar País do Filme")
        cursor.execute("SELECT show_id FROM filmes")
        resultado = cursor.fetchall()
        valores_filmes = {id[0] for id in resultado}

        with st.form(key="include_pais"):
            input_nome_pais = st.text_input(label="Insira nome do país")
            input_id_filme = st.selectbox(label="Selecione o id Do filme",options=valores_filmes)
            input_button_submit = st.form_submit_button('Cadastrar')
        if input_button_submit:
            if len(input_nome_pais) != 0:
                query = "INSERT INTO pais_filme (nome_pais, show_id) VALUES (%s, %s)"
                values = (input_nome_pais, input_id_filme)
                cursor.execute(query, values)
                cnx.commit()

                st.success("Diretor adicionado com sucesso!")
                st.info(f'Nome do País: {input_nome_pais}')
                st.info(f'Id do Filme: {input_id_filme}')

                st.warning('Atualizando página')
                st.experimental_rerun()

            elif len(input_nome_pais) == 0:
                st.warning('Você deve inserir o Nome do País')


    cursor.close()
    cnx.close()

def main():
    cadastrar()

if __name__ == "__main__":
    main()
