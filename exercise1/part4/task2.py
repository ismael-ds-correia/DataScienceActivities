import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder, MinMaxScaler, OneHotEncoder

# Carregar o dataset
penguins = sns.load_dataset("penguins")

# 1. TRATAMENTO DE VALORES NULOS
# Para colunas numéricas: preenchendo com a mediana.
numeric_cols = ['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g']
for col in numeric_cols:
    penguins.loc[:, col] = penguins[col].fillna(penguins[col].median())

# Para colunas categóricas: preenchendo com o a moda.
categorical_cols = ['species', 'island', 'sex']
for col in categorical_cols:
    penguins.loc[:, col] = penguins[col].fillna(penguins[col].mode())

# 2. TRATAMENTO DE VALORES CATEGÓRICOS
# Método 1: Label Encoding (para colunas ordinais ou binárias)
label_encoder = LabelEncoder()
penguins['sex_encoded'] = label_encoder.fit_transform(penguins['sex'])

# Método 2: One-Hot Encoding (para categorias sem ordem inerente)
penguins_encoded = pd.get_dummies(penguins, columns=['species', 'island'], drop_first=False)

# print(penguins_encoded.head())

# 3. NORMALIZAÇÃO DAS COLUNAS NUMÉRICAS (valores entre 0 e 1)

# Inicializando o MinMaxScaler
scaler = MinMaxScaler()

# Aplicando a normalização
penguins_encoded[numeric_cols] = scaler.fit_transform(penguins_encoded[numeric_cols])

# print(penguins_encoded[numeric_cols].head())

penguins_encoded.to_csv('penguins_normalized.csv', index=False)

# 4. SEPARAR O DATASET E X (FEATURES) E Y (TARGET)
# Usando a coluna 'species' como target
y_species = penguins['species']  # Guardamos a coluna target original

# Criando X: todas as features, excluindo a coluna target original e quaisquer colunas derivadas da target
# Também removemos colunas que não desejamos como features (como 'sex', pois já temos 'sex_encoded')
X = penguins_encoded.drop(columns=[
    'sex',  # Colunas originais que não queremos como features
    'species_Adelie', 'species_Chinstrap', 'species_Gentoo'  # Colunas one-hot da target
])

# Verificando as dimensões
print(f"\nDimensões de X (features): {X.shape}")
print(f"Dimensões de y (target): {y_species.shape}")

# Visualizar as primeiras linhas
print("\nPrimeiras linhas de X (features):")
print(X.head())
print("\nPrimeiras linhas de y (target):")
print(y_species.head())