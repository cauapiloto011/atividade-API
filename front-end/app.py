import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"
st.set_page_config(page_title="Gerenciador de produtos", page_icon="📦🧾")
st.title("📦 Estoque de produtos ")

menu = st.sidebar.radio("Navegação", ["Estoque", "Registrar produto", "Atualizar produto", "Deletar produto"])

if menu == "Estoque":
    st.subheader("Todos os filmes disponiveis")
    response = requests.get(f"{API_URL}/listar_produtos")
    if response.status_code == 200:
        produtos = response.json().get("produtos", [])
        if produtos:
            st.dataframe(produtos)
        else:
            st.info("❌ Não há produtos registrados")
    else:
        st.error("❌ Erro ao acessar a API")

elif menu == "Registrar produto":
    st.subheader("➕Adicionar produto")
    nome = st.text_input("Nome")
    categoria = st.text_input("categoria")
    preco = st.number_input("preco", min_value=1.1, step=0.1)
    quantidade = st.number_input("quantidade", min_value=1, step=1)
    if st.button("Adicionar produto"):
        dados = {"nome": nome, "categoria": categoria, "preco": preco, "quantidade": quantidade}
        response = requests.post(f"{API_URL}/produtos", params=dados)
        if response.status_code == 200:
            st.success("Produto adicionado com sucesso!")
        else:
            st.error("❌Erro ao adicionar produto")

elif menu == "Atualizar produto":
    st.subheader("🔂Atualizar produto")
    id_produto = st.number_input("ID do produto que deseja atualizar", min_value=1, step=1)
    novo_nome = st.text_input("Nome ( Se não for atualizar esse campo, coloque as informções antigas )")
    nova_categoria = st.text_input("Categoria ( Se não for atualizar esse campo, coloque as informções antigas )")
    novo_preco = st.number_input("Preço ( Se não for atualizar esse campo, coloque as informções antigas )", min_value=1.0, step=0.1)
    nova_quantidade = st.number_input("Quantidade ( Se não for atualizar esse campo, coloque as informções antigas )", min_value=1, step=1)
    if st.button("Atualizar produto"):
        dados = {"id_produto": id_produto, "novo_nome": novo_nome, "nova_categoria": nova_categoria, "novo_preco": novo_preco, "nova_quantidade": nova_quantidade}
        response = requests.put(f"{API_URL}/produtos/{id_produto}", params=dados)
        if response.status_code == 200:
            st.success("Registro atualizado com sucesso! ✔")
        else:
            st.error("❌ Erro ao atualizar registro")

elif menu == "Deletar produto":
    st.subheader("❌Deletar produto")
    id_produto = st.number_input("ID do produto que deseja atualizar", min_value=1, step=1)
    if st.button("Deletar produto"):
        dados = {"id_produto": id_produto}
        response = requests.delete(f"{API_URL}/produtos/{id_produto}", params=dados)
        if response.status_code == 200:
            st.success("Produto deletado com sucesso! ✔")
        else:
            st.error("❌ Erro ao deletar produto")
