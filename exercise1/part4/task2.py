import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder, OneHotEncoder

# Carregar o dataset
penguins = sns.load_dataset("penguins")

# Verificar a estrutura do dataset
print("Informações do dataset:")
print(penguins.info())

# Verificar estatísticas descritivas
print("\nEstatísticas descritivas:")
print(penguins.describe())

# Verificar valores nulos
print("\nValores nulos por coluna:")
print(penguins.isnull().sum())