import pandas as pd

data1 = {
    'TIME': ['Campinense', 'Naútico', 'Santos'],
    'TORCEDORES': [604564, 765298, 890765]
}

teams_df1 = pd.DataFrame(data1)

data2 = {
    'TIME': ['Vitoria', 'Internacional'],
    'TORCEDORES': [1920613, 1678943]
}

teams_df2 = pd.DataFrame(data2, index=[4, 5])

print(teams_df1)
print(teams_df2)