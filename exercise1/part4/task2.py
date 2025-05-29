import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder, OneHotEncoder

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

penguins_encoded.to_csv('penguins_treated.csv', index=False)