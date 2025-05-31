#5.3 Faça o POS Tagging (Classifica cada token do texto em uma classe gramatical)
import spacy
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

nlp = spacy.load("pt_core_news_sm")

texto = """a ana lis mora em uma cidade linda chamada joao pessoa
  humanos compram livros e ana lis comprou um livro sobre biologia marinha
  o joao leu o jornal na biblioteca durante a manha o poeta escreveu uma carta
  para o professor da faculdade e para seus discipulos o cachorro da ana lis
  perseguiu um gato no quintal lembrando que gatos sao felinos e cachorros sao
  caninos a professora explicou ou ensinou o conteudo da aula para os alunos o 
  menino comeu uma maca depois do almoco o carteiro entregou uma encomenda para
  a vizinha a vaca comeu o capim do pasto e por isso e herbivora e nao e carnivora
  o medico examinou o paciente com cuidado no consultorio o artista pintou um 
  quadro no atelie"""

doc = nlp(texto)

# Criar lista para armazenar os tokens e as classes gramaticais
pos_tags = []

for token in doc:
    print(f'{token.text}\t{token.pos_}')
    pos_tags.append((token.text, token.pos_))  # Armazenando na lista

df_pos = pd.DataFrame(pos_tags, columns=['Token', 'POS'])

# Salvar o DataFrame em CSV
df_pos.to_csv('pos_tags.csv', index=False)

df_pos = pd.read_csv('pos_tags.csv')

# Contar frequência de cada classe gramatical
pos_counts = df_pos['POS'].value_counts()

# Plotar gráfico de barras
plt.figure(figsize=(10,6))
sns.barplot(x=pos_counts.index, y=pos_counts.values, palette="viridis")
plt.title('Frequência das Classes Gramaticais')
plt.xlabel('Classe Gramatical')
plt.ylabel('Frequência')
plt.xticks(rotation=45)
plt.show()