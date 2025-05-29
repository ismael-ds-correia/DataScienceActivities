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
    penguins[col].fillna(penguins[col].median(), inplace=True)

# Para colunas categóricas: preenchendo com o a moda.
categorical_cols = ['species', 'island', 'sex']
for col in categorical_cols:
    penguins[col].fillna(penguins[col].mode()[0], inplace=True)

# Verificar se ainda existem valores nulos
print("\nValores nulos após tratamento:")
print(penguins.isnull().sum())