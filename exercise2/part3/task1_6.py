# 5.6 Apresente as entidades nomeadas
import spacy
import matplotlib.pyplot as plt
import seaborn as sns

nlp = spacy.load("pt_core_news_md")

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

df_ent = pd.DataFrame([(ent.text, ent.label_) for ent in doc.ents], 
                      columns=['Entidade', 'Tipo'])
df_ent.to_csv('entidades.csv', index=False)

# Mostrar entidades encontradas
for ent in doc.ents:
    print(f'{ent.text}\t{ent.label_}')