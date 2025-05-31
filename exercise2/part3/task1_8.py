#5.8 Extraia as relações (Análise de dependência) do corpus. Ex: Sujeito – Predicado
#– Objeto. Crie automaticamente um Dataset dos resultados dessa etapa. 
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

# Lista para guardar as relações
relacoes = []

for sent in doc.sents:
    sujeito = None
    verbo = None
    objeto = None
    for token in sent:
        if "subj" in token.dep_:
            sujeito = token.text
        if token.pos_ == "VERB":
            verbo = token.lemma_
        if "obj" in token.dep_:
            objeto = token.text
    if sujeito and verbo:
        relacoes.append({
            'Sujeito': sujeito,
            'Predicado': verbo,
            'Objeto': objeto
        })

df_relacoes = pd.DataFrame(relacoes)
df_relacoes.to_csv('relacoes.csv', index=False)

print(df_relacoes)