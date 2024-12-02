SQL_CRIAR_TABELA = """
    CREATE TABLE IF NOT EXISTS produto (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        preco FLOAT NOT NULL,
        descricao TEXT NOT NULL,
<<<<<<< HEAD
        estoque INTEGER NOT NULL,
        id_categoria INTEGER NOT NULL,
        FOREIGN KEY (id_categoria) REFERENCES categoria(id))
"""

SQL_INSERIR = """
    INSERT INTO produto(nome, preco, descricao, estoque, id_categoria)
    VALUES (?, ?, ?, ?, ?)
"""

SQL_OBTER_TODOS = """
    SELECT id, nome, preco, descricao, estoque, id_categoria
=======
        estoque INTEGER NOT NULL)
"""

SQL_INSERIR = """
    INSERT INTO produto(nome, preco, descricao, estoque)
    VALUES (?, ?, ?, ?)
"""

SQL_OBTER_TODOS = """
    SELECT id, nome, preco, descricao, estoque
>>>>>>> aae658d356c8ba08adc33219f8cb390ce4cb0981
    FROM produto
    ORDER BY nome
"""

SQL_ALTERAR = """
    UPDATE produto
<<<<<<< HEAD
    SET nome=?, preco=?, descricao=?, estoque=?, id_categoria=?
=======
    SET nome=?, preco=?, descricao=?, estoque=?
>>>>>>> aae658d356c8ba08adc33219f8cb390ce4cb0981
    WHERE id=?
"""

SQL_EXCLUIR = """
    DELETE FROM produto    
    WHERE id=?
"""

SQL_OBTER_UM = """
<<<<<<< HEAD
    SELECT id, nome, preco, descricao, estoque, id_categoria
=======
    SELECT id, nome, preco, descricao, estoque
>>>>>>> aae658d356c8ba08adc33219f8cb390ce4cb0981
    FROM produto
    WHERE id=?
"""

SQL_OBTER_QUANTIDADE = """
    SELECT COUNT(*) FROM produto
"""

SQL_OBTER_BUSCA = """
    SELECT id, nome, preco, descricao, estoque
    FROM produto
    WHERE nome LIKE ? OR descricao LIKE ?
    ORDER BY #1
    LIMIT ? OFFSET ?
"""

SQL_OBTER_QUANTIDADE_BUSCA = """
    SELECT COUNT(*) FROM produto
    WHERE nome LIKE ? OR descricao LIKE ?
"""