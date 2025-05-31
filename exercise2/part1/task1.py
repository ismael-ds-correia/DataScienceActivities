import pandas as pd
import numpy as np

# Criar DataFrame Usuario
np.random.seed(42)  # Para reprodutibilidade
nomes = ['Ana Lis', 'Bruno', 'Carlos', 'Daniela', 'Eduardo', 'Flávia', 'Gabriel', 
         'Helena', 'Igor', 'Joana', 'Kevin', 'Laura', 'Mateus', 'Natália', 
         'Otávio', 'Paula', 'Quincy', 'Roberto', 'Sofia', 'Tiago', 'Ursula', 
         'Vitor', 'Wilma', 'Xavier', 'Yasmin', 'Zé']

usuarios = {
    'id': list(range(1, len(nomes) + 1)),
    'nome': nomes,
    'idade': np.random.randint(14, 65, len(nomes)),
    'pk': list(range(1, len(nomes) + 1))
}

df_usuario = pd.DataFrame(usuarios)

# Criar DataFrame Cidade
cidades = ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Salvador', 'Brasília',
           'Fortaleza', 'Recife', 'Porto Alegre', 'Curitiba', 'Manaus', 'São Paulo',
           'Rio de Janeiro', 'Belo Horizonte', 'Salvador', 'Brasília',
           'São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Salvador', 'Brasília',
           'Fortaleza', 'Recife', 'Porto Alegre', 'Curitiba', 'Manaus', 'São Paulo']

estados = ['SP', 'RJ', 'MG', 'BA', 'DF', 'CE', 'PE', 'RS', 'PR', 'AM', 'SP',
           'RJ', 'MG', 'BA', 'DF', 'SP', 'RJ', 'MG', 'BA', 'DF', 'CE', 'PE', 
           'RS', 'PR', 'AM', 'SP']

cidades_data = {
    'id': list(range(1, len(nomes) + 1)),
    'nome': cidades,
    'estado': estados,
    'pk': list(range(1, len(nomes) + 1))  # Mesma PK para simular um relacionamento 1:1
}

df_cidade = pd.DataFrame(cidades_data)

# SQL: SELECT nome, idade FROM Usuario
result = df_usuario[['nome', 'idade']]
print(result.head())