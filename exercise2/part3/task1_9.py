#5.9 Verifique os resultados e apresente o percentual de acerto e erro do sistema. 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df_relacoes = pd.read_csv('relacoes.csv')

total = len(df_relacoes)
corretos = df_relacoes.dropna(subset=['Sujeito', 'Predicado']).shape[0]
erros = total - corretos

# Percentuais
percentual_acerto = (corretos / total) * 100 if total > 0 else 0
percentual_erro = (erros / total) * 100 if total > 0 else 0

print(f"Total de relações: {total}")
print(f"Acertos: {corretos} ({percentual_acerto:.2f}%)")
print(f"Erros: {erros} ({percentual_erro:.2f}%)")

df_resultado = pd.DataFrame([{
    'Total': total,
    'Acertos': corretos,
    'Erros': erros,
    'Percentual Acerto': percentual_acerto,
    'Percentual Erro': percentual_erro
}])

df_resultado.to_csv('resultado_avaliacao.csv', index=False)