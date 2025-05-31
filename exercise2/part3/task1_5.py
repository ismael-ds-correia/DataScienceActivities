#5.5 Apresente as dependências sintáticas
import spacy
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

df_dep = pd.DataFrame([(token.text, token.dep_, token.head.text) for token in doc], 
                      columns=['Token', 'Dependência', 'Head'])
df_dep.to_csv('dependencias.csv', index=False)

# Mostrar token, dependência sintática, palavra cabeça
for token in doc:
    print(f'{token.text}\t{token.dep_}\t{token.head.text}')

# Contar a frequência das dependências sintáticas
freq_dep = df_dep['Dependência'].value_counts()

# Plotar gráfico de barras
plt.figure(figsize=(12,6))
sns.barplot(x=freq_dep.index, y=freq_dep.values, palette='magma')
plt.title('Frequência das Dependências Sintáticas')
plt.xlabel('Tipo de Dependência')
plt.ylabel('Frequência')
plt.xticks(rotation=45)
plt.show()