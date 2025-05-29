import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder, MinMaxScaler, OneHotEncoder
from sklearn.model_selection import train_test_split

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

# 4. SEPARAR O DATASET EM X (FEATURES) E Y (TARGET)
# Usando a coluna 'species' como target
y_species = penguins['species']  # Guardamos a coluna target original

# Criando X: todas as features, excluindo a coluna target original e quaisquer colunas derivadas da target
# Também removemos colunas que não desejamos como features (como 'sex', pois já temos 'sex_encoded')
X = penguins_encoded.drop(columns=[
    'sex',  # Colunas originais que não queremos como features
    'species_Adelie', 'species_Chinstrap', 'species_Gentoo'  # Colunas one-hot da target
])

# 5. DIVIDIR OS DADOS EM CONJUNTOS DE TREINAMENTO E TESTE
# Definindo a proporção: 80% para treino e 20% para teste
test_size = 0.2  # 20% para teste (80% para treino)

# Dividindo os dados mantendo a proporção das classes (stratify)
X_train, X_test, y_train, y_test = train_test_split(
    X, y_species, 
    test_size=test_size,
    random_state=42,  # Para reprodutibilidade
    stratify=y_species  # Mantém a mesma proporção de cada espécie nos conjuntos
)

# Verificando as dimensões dos conjuntos de treino e teste
print("\nConjuntos de Treino e Teste:")
print(f"X_train: {X_train.shape} ({100-test_size*100:.0f}% dos dados)")
print(f"X_test: {X_test.shape} ({test_size*100:.0f}% dos dados)")
print(f"y_train: {y_train.shape} ({100-test_size*100:.0f}% dos dados)")
print(f"y_test: {y_test.shape} ({test_size*100:.0f}% dos dados)")

# Verificando a distribuição das classes (espécies) nos conjuntos
print("\nDistribuição das espécies:")
print(f"Dataset completo:\n{y_species.value_counts()}")
print(f"Conjunto de treino:\n{y_train.value_counts()}")
print(f"Conjunto de teste:\n{y_test.value_counts()}")