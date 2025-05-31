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

# SQL: SELECT * FROM Usuario WHERE idade > 35
result = df_usuario[df_usuario['idade'] > 35]
print(result.head())

# SQL: SELECT * FROM Usuário Us INNER JOIN Cidade Ci ON Us.pk = Ci.pk
result = pd.merge(df_usuario, df_cidade, on='pk')
print(result.head())

# SQL: SELECT nome, estado, COUNT(*) FROM Cidade GROUP BY estado
result = df_cidade.groupby('estado').agg({'nome': 'count'}).reset_index()
result.columns = ['estado', 'contagem']
print(result)

# SQL: SELECT estado, SUM(idade) FROM Usuário Us INNER JOIN Cidade Ci ON Us.pk = Ci.pk GROUP BY estado
merged = pd.merge(df_usuario, df_cidade, on='pk')
result = merged.groupby('estado')['idade'].sum().reset_index()
print(result)

# SQL: SELECT * FROM Usuario ORDER BY idade
result = df_usuario.sort_values(by='idade')
print(result.head())

# SQL: SELECT * FROM Usuario LIMIT 3
result = df_usuario.head(3)
print(result)

# SQL: SELECT * FROM Usuario ORDER BY idade DESC LIMIT 6
result = df_usuario.sort_values(by='idade', ascending=False).head(6)
print(result)

# Quantas linhas tem a tabela Usuário e a tabela Cidade? (COUNT)
# SQL: SELECT COUNT(*) FROM Usuario; SELECT COUNT(*) FROM Cidade
print(f"Número de registros na tabela Usuario: {len(df_usuario)}")
print(f"Número de registros na tabela Cidade: {len(df_cidade)}")

# Qual a média das idades dos Usuários? (AVG)
# SQL: SELECT AVG(idade) FROM Usuario
mean_age = df_usuario['idade'].mean()
print(f"Média das idades dos usuários: {mean_age:.2f}")

# Qual a soma das idades dos Usuários? (SUM)
# SQL: SELECT SUM(idade) FROM Usuario
sum_age = df_usuario['idade'].sum()
print(f"Soma das idades dos usuários: {sum_age}")

# SQL: SELECT * FROM Usuario WHERE idade IN (19,47)
result = df_usuario[df_usuario['idade'].isin([19, 47])]
print(result)

# SQL: SELECT * FROM Usuario WHERE idade NOT IN (19,47)
result = df_usuario[~df_usuario['idade'].isin([19, 47])]
print(result.head())

# SQL: SELECT * FROM Usuario WHERE idade BETWEEN 23 AND 50
result = df_usuario[(df_usuario['idade'] >= 23) & (df_usuario['idade'] <= 50)]
print(result.head())

# SQL: SELECT DISTINCT estado FROM Cidade
result = df_cidade['estado'].unique()
print(result)

# SQL: SELECT DISTINCT nome, estado FROM Cidade
result = df_cidade[['nome', 'estado']].drop_duplicates()
print(result.head())

# SQL: SELECT id, nome, idade, CASE WHEN idade > 18 THEN 'ADULTO' ELSE 'ADOLESCENTE' END AS categoria FROM Usuario
df_usuario['categoria'] = df_usuario['idade'].apply(lambda x: 'ADULTO' if x > 18 else 'ADOLESCENTE')
result = df_usuario[['id', 'nome', 'idade', 'categoria']]
print(result.head())

# SQL: SELECT estado, COUNT(*) FROM Cidade GROUP BY estado HAVING COUNT(*) > 1
estado_counts = df_cidade.groupby('estado').size().reset_index(name='contagem')
result = estado_counts[estado_counts['contagem'] > 1]
print(result)

# SQL: SELECT * FROM (SELECT * FROM Usuario WHERE idade > 31) WHERE nome LIKE 'A%'
subquery = df_usuario[df_usuario['idade'] > 31]
result = subquery[subquery['nome'].str.startswith('A')]
print(result)

# SQL: SELECT * FROM Usuario WHERE nome LIKE 'a%'
result = df_usuario[df_usuario['nome'].str.lower().str.startswith('a')]
print(result)

# SQL: ALTER TABLE Usuario ADD COLUMN sobrenome VARCHAR
df_usuario['sobrenome'] = None  # Adiciona coluna com valores nulos
print(df_usuario.head())

# SQL: UPDATE Usuario SET idade = idade + 1 WHERE nome = 'Ana Lis'
df_usuario.loc[df_usuario['nome'] == 'Ana Lis', 'idade'] += 1
print(df_usuario[df_usuario['nome'] == 'Ana Lis'])

# SQL: DELETE FROM Usuario WHERE idade < 15
df_usuario = df_usuario[df_usuario['idade'] >= 15]
print(f"Número de registros após a exclusão: {len(df_usuario)}")

# SQL: CREATE INDEX idx_nome ON Usuario (nome)
df_usuario.set_index('nome', inplace=True)
print(df_usuario.head())

# Revertendo e voltando ao DataFrame original:
df_usuario.reset_index(inplace=True)

# SQL: SELECT id, nome FROM Usuario UNION SELECT id, nome FROM Cidade

# UNION (equivalente a pd.concat com drop_duplicates)
union_result = pd.concat([
    df_usuario[['id', 'nome']],
    df_cidade[['id', 'nome']]
]).drop_duplicates()
print(union_result.head())

# UNION ALL (equivalente a pd.concat sem drop_duplicates)
union_all_result = pd.concat([
    df_usuario[['id', 'nome']],
    df_cidade[['id', 'nome']]
])
print(union_all_result.head())