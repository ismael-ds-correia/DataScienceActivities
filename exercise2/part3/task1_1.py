import re
from unidecode import unidecode

texto = """A Ana Lis mora em uma cidade linda, chamada João Pessoa.
Humanos compram livros e Ana Lis comprou um livro sobre biologia marinha.
O João leu o jornal na biblioteca durante a manhã.
O poeta escreveu uma carta para o professor da faculdade e para seus discípulos.
O cachorro da Ana <Lis> perseguiu um gato no quintal, lembrando que gatos são felinos e cachorros são caninos*.
A professora explicou ou ensinou o conteúdo da aula para os alunos. O menino comeu uma maçã depois do almoço.
O carteiro entregou uma encomenda para a vizinha. A vaca comeu o capim do pasto e por isso é herbívora e não é carnívora.
O médico examinou o paciente com cuidado no consultório. [O artista pintou um quadro no ateliê]."""

#Remover acentos
texto_sem_acentos = unidecode(texto)

#Converter para minúsculas
texto_minusculo = texto_sem_acentos.lower()

#Remover tags e símbolos <>, [], *, etc
texto_sem_tags = re.sub(r'[\[\]\<\>\*\^]', '', texto_minusculo)

#Remover pontuação
texto_sem_pontuacao = re.sub(r'[^\w\s]', '', texto_sem_tags)

#Remover números
texto_sem_numeros = re.sub(r'\d+', '', texto_sem_pontuacao)

#Remover palavras redundantes consecutivas (exemplo "Ana Ana")
def remove_redundant_words(text):
    tokens = text.split()
    resultado = []
    for i, token in enumerate(tokens):
        if i == 0 or token != tokens[i-1]:
            resultado.append(token)
    return ' '.join(resultado)

texto_final = remove_redundant_words(texto_sem_numeros)

print(texto_final)