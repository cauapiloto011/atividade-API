if menu == "Adicionar filmes":
    st.subheader("🗓Adicionar filmes")
    titulo = st.text_input ("Titulo do Filme")
    genero = st.text-input("Genero")
    ano = st.number_input("Ano de Lançamento", min_value=1880, max_value=2100, step=0.1)
    avaliacao = st.number_input("Avaliação de (0 a 10)", min_value=0.0, max_value1=0.0, step=0.1)
    if st.button("Salvar Filme"):
        dados = {titulo: titulo, "genero": genero, "ano": ano, "avaliacao": avaliacao}
        response = requests.post(F"{API_URL}/filmes", params=dados)
        if response.status_code == 200:
            st.sucess("Filme adicionando com sucesso!")
        else:
            st.error("Erro ao adicionar o filme")


@app.put("/filmes/{id_filmes}")
def atualizar_filme(id_filme, nova_avaliacao):
    funcao.atualizar
