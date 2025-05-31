# 5.7 Crie automaticamente um Dataset dos resultados do seu sistema, organize por
#classe gramatical. 
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

dados = []

for token in doc:
    dados.append({
        'Token': token.text,
        'Classe_Gramatical': token.pos_,
        'Lema': token.lemma_
    })

df = pd.DataFrame(dados)

df_ordenado = df.sort_values(by='Classe_Gramatical')

# Exibir as primeiras linhas
print(df_ordenado.head(20))

df_ordenado.to_csv('classe_gramatical.csv', index=False)

freq_pos = df_ordenado['Classe_Gramatical'].value_counts()

plt.figure(figsize=(12,6))
sns.barplot(x=freq_pos.index, y=freq_pos.values, palette='viridis')
plt.title('Frequência das Classes Gramaticais (POS tags)')
plt.xlabel('Classe Gramatical')
plt.ylabel('Frequência')
plt.xticks(rotation=45)
plt.show()