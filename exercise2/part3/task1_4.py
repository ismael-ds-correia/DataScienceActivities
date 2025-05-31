#5.4 Transforme os textos usando lematização. Sabe o que é lematização?
#Exemplo: correram → correr → Verbo | casas → casa → substantivo
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

# Criar lista para armazenar os lemas
lemmas = []

# Mostrar token, classe gramatical e lema
for token in doc:
    print(f'{token.text}\t{token.pos_}\t{token.lemma_}')
    lemmas.append({'Token': token.text, 'Classe_Gramatical': token.pos_, 'Lemma': token.lemma_})

# Criar DataFrame com todas as informações
df_lemmas = pd.DataFrame(lemmas)

# Salvar em CSV
df_lemmas.to_csv('lemmas.csv', index=False)

df_lemmas = pd.read_csv('lemmas.csv')

# Contar frequência de lemas
lemma_counts = df_lemmas['Lemma'].value_counts().head(10)  # Top 10 lemas

# Plotar
plt.figure(figsize=(10,6))
sns.barplot(x=lemma_counts.index, y=lemma_counts.values, palette="magma")
plt.title('Top 10 Lemas mais Frequentes')
plt.xlabel('Lema')
plt.ylabel('Frequência')
plt.xticks(rotation=45)
plt.show()