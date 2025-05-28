import pandas as pd

data = [
    {'TIME': 'Liverpool', 'PAÍS': 'Inglaterra', 'TORCEDORES': 60456478, 'MÉDIA SALARIAL': 198000},
    {'TIME': 'Santa Cruz', 'PAÍS': 'Brasil', 'TORCEDORES': 951, 'MÉDIA SALARIAL': 10000},
    {'TIME': 'Milan', 'PAÍS': 'Itália', 'TORCEDORES': 890765667, 'MÉDIA SALARIAL': 110369},
    {'TIME': 'Frankfurt', 'PAÍS': 'Alemanha', 'TORCEDORES': 149087, 'MÉDIA SALARIAL': 97236},
    {'TIME': 'All Nassr', 'PAÍS': 'Arabia Saudita', 'TORCEDORES': 30000, 'MÉDIA SALARIAL': 214236}
]

df = pd.DataFrame(data)

print(df.dtypes)