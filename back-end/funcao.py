from conexao import conectar

def criar_produto():
    conexao, cursor = conectar()
    if conexao:
        try:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS produto (
                id SERIAL PRIMARY KEY,
                titulo TEXT NOT NULL,
                genero TEXT NOT NULL,
                ano INTEGER NOT NULL,
                avaliacao REAL          
                )           
            """)
            conexao.commit()
        except Exception as erro:
            print(f"Erro ao criar o produto {erro}")
        finally:
            cursor.close()
            conexao.close()
            
criar_produto()