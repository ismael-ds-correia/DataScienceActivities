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

combined_df = pd.concat([teams_df1, teams_df2])

print(combined_df)

# Salvar em .csv
teams_df1.to_csv('teams_df1.csv', index=False)
teams_df2.to_csv('teams_df2.csv', index=False)
combined_df.to_csv('combined_teams.csv', index=False)

# Salvar em .html
teams_df1.to_html('teams_df1.html', index=False)
teams_df2.to_html('teams_df2.html', index=False)
combined_df.to_html('combined_teams.html', index=False)

# Salvar em formato .json
teams_df1.to_json('times_df1.json')
teams_df2.to_json('times_df2.json')
combined_df.to_json('times_combined.json')