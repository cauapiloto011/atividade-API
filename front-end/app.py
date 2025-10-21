API_URL = "http://127.0.0.1:8000"
st.set_page_config(page_title="Gerenciador de produtos", page_icon="📦🧾")
st.title("📦 Estoque de produtos ")

menu = st.sidebar.radio("Navegação", ["Estoque", "Registrar produto", "Atualizar produto", "Deletar produto"])

