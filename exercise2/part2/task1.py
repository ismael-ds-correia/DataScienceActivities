import pandas as pd
import numpy as np

# Criar o DataFrame com valores ausentes e espaços em branco
df = pd.DataFrame({
    'A': [1, np.nan, 3, np.nan, " "],
    'B': [4, np.nan, np.nan, np.nan, 3],
    'C': [7, np.nan, 9, np.nan, 11],
    'D': [5, 4, 9, np.nan, " "]
})

# Exibindo o DataFrame original
print("DataFrame original:")
print(df)

# Exibindo a quantidade de dados ausentes em cada coluna originalmente
print("\nQuantidade de dados ausentes por coluna (original):")
print(df.isna().sum())

# Remover linhas com qualquer valor ausente (how='any' é o padrão)
df_sem_na_original = df.dropna()
print("\nDataFrame após remover linhas com qualquer valor ausente (original):")
print(df_sem_na_original)

# Removendo apenas linhas onde TODOS os valores são ausentes
df_all_na_original = df.dropna(how='all')
print("\nDataFrame após remover linhas com TODOS os valores ausentes (original):")
print(df_all_na_original)

# Agora, substituindo espaços em branco por NaN
df_modificado = df.replace(" ", np.nan, regex=False)
print("\n----- APÓS SUBSTITUIÇÃO DE ESPAÇOS EM BRANCO -----")

print("\nDataFrame após substituir espaços em branco por NaN:")
print(df_modificado)

# Exibindo a quantidade de dados ausentes após substituição
print("\nQuantidade de dados ausentes por coluna (após substituição):")
print(df_modificado.isna().sum())

# Remover linhas com qualquer valor ausente (how='any' é o padrão)
df_sem_na_modificado = df_modificado.dropna()
print("\nDataFrame após remover linhas com qualquer valor ausente (após substituição):")
print(df_sem_na_modificado)

# Removendo apenas linhas onde TODOS os valores são ausentes
df_all_na_modificado = df_modificado.dropna(how='all')
print("\nDataFrame após remover linhas com TODOS os valores ausentes (após substituição):")
print(df_all_na_modificado)

# Análise das diferenças
print("\n----- ANÁLISE DOS RESULTADOS -----")
print(f"Número de valores ausentes originais: {df.isna().sum().sum()}")
print(f"Número de valores ausentes após substituição: {df_modificado.isna().sum().sum()}")
print(f"Diferença: {df_modificado.isna().sum().sum() - df.isna().sum().sum()} valores adicionais")

print(f"\nLinhas restantes após dropna(how='any') original: {len(df_sem_na_original)}")
print(f"Linhas restantes após dropna(how='any') com substituição: {len(df_sem_na_modificado)}")

print(f"\nLinhas restantes após dropna(how='all') original: {len(df_all_na_original)}")
print(f"Linhas restantes após dropna(how='all') com substituição: {len(df_all_na_modificado)}")