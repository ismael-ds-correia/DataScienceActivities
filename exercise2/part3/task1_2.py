#5.2 Faça uma Tokenização (Separar o texto em tokens)
import nltk
nltk.download('punkt_tab')

from nltk.tokenize import word_tokenize

#Usando o texto limpo da etapa anterior:
texto_limpo = """a ana lis mora em uma cidade linda chamada joao pessoa
  humanos compram livros e ana lis comprou um livro sobre biologia marinha
  o joao leu o jornal na biblioteca durante a manha o poeta escreveu uma carta
  para o professor da faculdade e para seus discipulos o cachorro da ana lis
  perseguiu um gato no quintal lembrando que gatos sao felinos e cachorros sao
  caninos a professora explicou ou ensinou o conteudo da aula para os alunos o 
  menino comeu uma maca depois do almoco o carteiro entregou uma encomenda para
  a vizinha a vaca comeu o capim do pasto e por isso e herbivora e nao e carnivora
  o medico examinou o paciente com cuidado no consultorio o artista pintou um 
  quadro no atelie"""

tokens = word_tokenize(texto_limpo)

# Salvar tokens em CSV
df_tokens = pd.DataFrame(tokens, columns=['Token'])
df_tokens.to_csv('tokens.csv', index=False)

print(tokens)