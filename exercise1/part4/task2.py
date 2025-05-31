import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder, MinMaxScaler, OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from imblearn.over_sampling import SMOTE  # Para balanceamento de classes

penguins = sns.load_dataset("penguins")

# 1. TRATAMENTO DE VALORES NULOS
# Para colunas numéricas: preenchendo com a mediana.
numeric_cols = ['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g']
for col in numeric_cols:
    penguins.loc[:, col] = penguins[col].fillna(penguins[col].median())

# Para colunas categóricas: preenchendo com o a moda.
categorical_cols = ['species', 'island', 'sex']
for col in categorical_cols:
    penguins.loc[:, col] = penguins[col].fillna(penguins[col].mode()[0])  # Adicionado [0] para obter o primeiro valor da moda

# 2. TRATAMENTO DE VALORES CATEGÓRICOS
# Método 1: Label Encoding (para colunas ordinais ou binárias)
label_encoder = LabelEncoder()
penguins['sex_encoded'] = label_encoder.fit_transform(penguins['sex'])

# Método 2: One-Hot Encoding (para categorias sem ordem inerente)
penguins_encoded = pd.get_dummies(penguins, columns=['species', 'island'], drop_first=False)

# 3. NORMALIZAÇÃO DAS COLUNAS NUMÉRICAS (valores entre 0 e 1)
# Inicializando o MinMaxScaler
scaler = MinMaxScaler()

# Aplicando a normalização
penguins_encoded[numeric_cols] = scaler.fit_transform(penguins_encoded[numeric_cols])

penguins_encoded.to_csv('penguins_normalized.csv', index=False)

# 4. SEPARAR O DATASET EM X (FEATURES) E Y (TARGET)
# Usando a coluna 'species' como target
y_species = penguins['species']  # Guardamos a coluna target original

# Aplicar LabelEncoder no target (y_species) para converter strings em números
species_encoder = LabelEncoder()
y_species_encoded = species_encoder.fit_transform(y_species)

# Guardar o mapeamento das classes para uso posterior
species_names = species_encoder.classes_

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
    X, y_species_encoded,  # Usando a versão codificada do target
    test_size=test_size,
    random_state=42,  # Para reprodutibilidade
    stratify=y_species_encoded  # Usando a versão codificada para estratificação
)

# Aplicar SMOTE para balancear as classes (alternativa ao sample_weight)
try:
    smote = SMOTE(random_state=42)
    X_train_resampled, y_train_resampled = smote.fit_resample(X_train, y_train)
    print("Balanceamento de classes aplicado com SMOTE.")
    print(f"Amostras antes do SMOTE: {X_train.shape[0]}")
    print(f"Amostras após o SMOTE: {X_train_resampled.shape[0]}")
except ImportError:
    print("AVISO: Pacote 'imbalanced-learn' não encontrado. Usando dados originais.")
    X_train_resampled, y_train_resampled = X_train, y_train

# 6. TREINAR UM CLASSIFICADOR MLP
# Definindo uma topologia mais complexa
hidden_layer_sizes = (20, 15, 10)  # Três camadas ocultas com mais neurônios

# Função de ativação: tanh (alternativa ao ReLU para melhor performance)
activation = 'tanh'

# Número máximo de iterações (épocas)
max_iter = 1000

# Aumentar número de execuções para maior estabilidade
n_executions = 20
best_accuracy = 0
best_model = None

print("\nTREINAMENTO DO MODELO MLP")
print(f"Topologia da rede: {hidden_layer_sizes} (três camadas ocultas)")
print(f"Função de ativação: {activation}")
print(f"Número de execuções: {n_executions}")

# Realizar várias execuções para obter resultados estáveis
accuracies = []
for i in range(n_executions):
    # Criar o modelo MLP com parâmetros otimizados
    mlp = MLPClassifier(
        hidden_layer_sizes=hidden_layer_sizes,
        activation=activation,
        max_iter=max_iter,
        random_state=i,  # Diferentes seeds para cada execução
        early_stopping=True,  # Parar quando o erro não diminuir
        validation_fraction=0.1,  # 10% dos dados de treino para validação
        alpha=0.01,  # Adicionar regularização L2
        learning_rate='adaptive',  # Taxa de aprendizado adaptativa
        tol=1e-5  # Tolerância mais rigorosa
    )
    
    # Treinar o modelo com os dados balanceados
    mlp.fit(X_train_resampled, y_train_resampled)
    
    # Fazer previsões nos dados de teste
    y_pred = mlp.predict(X_test)
    
    # Calcular acurácia
    accuracy = accuracy_score(y_test, y_pred)
    accuracies.append(accuracy)
    
    # Manter o melhor modelo encontrado
    if accuracy > best_accuracy:
        best_accuracy = accuracy
        best_model = mlp

# Calcular média e desvio padrão das acurácias
mean_accuracy = np.mean(accuracies)
std_accuracy = np.std(accuracies)

print("\nResultados das execuções:")
print(f"Acurácia média: {mean_accuracy:.4f} ± {std_accuracy:.4f}")
print(f"Melhor acurácia: {best_accuracy:.4f}")

# Obter previsões do melhor modelo
y_pred_best = best_model.predict(X_test)

# Imprimir relatório de classificação detalhado usando os nomes das classes
print("\nRelatório de classificação:")
print(classification_report(y_test, y_pred_best, target_names=species_names, zero_division=0))

# Matriz de confusão
cm = confusion_matrix(y_test, y_pred_best)
plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', 
            xticklabels=species_names,  # Usando nomes das espécies em vez de valores numéricos
            yticklabels=species_names)
plt.xlabel('Previsão')
plt.ylabel('Valor Real')
plt.title('Matriz de Confusão')
plt.savefig('confusion_matrix.png')
plt.close()

# Visualização da acurácia ao longo das execuções
plt.figure(figsize=(10, 6))
plt.plot(range(1, n_executions + 1), accuracies, marker='o')
plt.axhline(y=mean_accuracy, color='r', linestyle='--', label=f'Média: {mean_accuracy:.4f}')
plt.xlabel('Número da Execução')
plt.ylabel('Acurácia')
plt.title('Acurácia ao longo das execuções')
plt.grid(True)
plt.legend()
plt.savefig('accuracy_runs.png')

# Criar um gráfico adicional: importância das características
plt.figure(figsize=(10, 6))
feature_importance = np.abs(best_model.coefs_[0]).mean(axis=1)
feature_names = X.columns
importance_df = pd.DataFrame({'Feature': feature_names, 'Importance': feature_importance})
importance_df = importance_df.sort_values('Importance', ascending=False)
sns.barplot(x='Importance', y='Feature', data=importance_df)
plt.title('Importância Relativa das Características')
plt.tight_layout()
plt.savefig('feature_importance.png')