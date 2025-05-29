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

print("DataFrame 1:")
print(teams_df1)
print("\nDataFrame 2:")
print(teams_df2)

# Combinar os DataFrames sem ignorar os índices
combined_keeping_index = pd.concat([teams_df1, teams_df2])
print("\nDataFrames combinados mantendo os índices originais:")
print(combined_keeping_index)

# Combinar os DataFrames ignorando os índices (reset_index)
combined_ignoring_index = pd.concat([teams_df1, teams_df2], ignore_index=True)
print("\nDataFrames combinados ignorando os índices:")
print(combined_ignoring_index) 