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

def inserir_produto(nome, categoria, preco, quantidade):
    conexao, cursor = conectar()
    if conexao:
        try:
            cursor.execute(
                "INSERT INTO produto (nome, categoria, preco, quantidade) VALUES (%s, %s, %s, %s)",
                (nome, categoria, preco, quantidade)
            )
            conexao.commit()
        except Exception as erro:
            print(f"Erro ao inserir produto {erro}")
        finally:
            cursor.close()
            conexao.close()
inserir_produto("BB", "ab", 2020, 9.0)   
def listar_filme():
    conexao, cursor = conectar()
    if conexao:
        try:
            cursor.execute(
                "SELECT * FROM produto ORDER BY id"
            )
            return cursor.fetchall()
        except Exception as erro:
            print(f"Erro ao inserir produto {erro}")
        finally:
            cursor.close()
            conexao.close()

def atualizar_produto(id_produto, nova_avaliacao):
    conexao, cursor = conectar()
    if conexao:
        try:
            cursor.execute(
                "UPDATE produto SET avaliacao = %s WHERE id = %s",
                (nova_avaliacao, id_produto)
            )
            conexao.commit()
        except Exception as erro:
            print(f"Erro ao tentar atualizar o produto {erro}")
        finally:
            cursor.close()
            conexao.close()

def deletar_produto(id_produto):
    conexao, cursor = conectar()
    if conexao:
        try:
            cursor.execute(
                "DELETE FROM produto WHERE id = %s",
                (id_produto,)
            )
            conexao.commit()
        except Exception as erro:
            print(f"Erro ao tentar deletar o produto {erro}")
        finally:
            cursor.close()
            conexao.close()