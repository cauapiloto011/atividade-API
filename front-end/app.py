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