import pandas as pd
import numpy as np

# Criar o DataFrame com valores ausentes e espaços em branco
df = pd.DataFrame({
    'A': [1, np.nan, 3, np.nan, " "],
    'B': [4, np.nan, np.nan, np.nan, 3],
    'C': [7, np.nan, 9, np.nan, 11],
    'D': [5, 4, 9, np.nan, " "]
})

# Exibindo a quantidade de dados ausentes em cada coluna
print(df.isna().sum())

# Remover linhas com qualquer valor ausente (how='any' é o padrão)
df_sem_na = df.dropna()
print(df_sem_na)

# Removendo apenas linhas onde TODOS os valores são ausentes
df_all_na = df.dropna(how='all')
print(df_all_na)

