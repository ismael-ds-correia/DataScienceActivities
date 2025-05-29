import pandas as pd

data = [
    {'TIME': 'Liverpool', 'PAÍS': 'Inglaterra', 'TORCEDORES': 60456478, 'MÉDIA SALARIAL': 198000},
    {'TIME': 'Santa Cruz', 'PAÍS': 'Brasil', 'TORCEDORES': 951, 'MÉDIA SALARIAL': 10000},
    {'TIME': 'Milan', 'PAÍS': 'Itália', 'TORCEDORES': 890765667, 'MÉDIA SALARIAL': 110369},
    {'TIME': 'Frankfurt', 'PAÍS': 'Alemanha', 'TORCEDORES': 149087, 'MÉDIA SALARIAL': 97236},
    {'TIME': 'All Nassr', 'PAÍS': 'Arabia Saudita', 'TORCEDORES': 30000, 'MÉDIA SALARIAL': 214236}
]

df = pd.DataFrame(data)

df['TORCEDORES'] = df['TORCEDORES'].astype(float)

dates = [
    '15/03/2010',
    '22/07/2015',
    '05/11/2008',
    '18/04/2022',
    '30/09/2019'
]

df['DATA'] = dates

df = df.rename(columns={'TORCEDORES': 'Nº TORCEDORES', 'DATA': 'DATA - CRIAÇÃO'})

# Criar um dicionário de mapeamento de países para siglas
country_codes = {
    'Inglaterra': 'ENG',
    'Brasil': 'BRA',
    'Itália': 'ITA',
    'Alemanha': 'GER',
    'Arabia Saudita': 'KSA'
}

# Criar a coluna SIGLA baseada no país
df['SIGLA'] = df['PAÍS'].map(country_codes)

sorted_by_country = df.sort_values(by='PAÍS')

print(sorted_by_country)