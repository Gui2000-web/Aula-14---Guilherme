# Solicitado um levantamento para compreender melhor o comportamento dos valores obtidos com as vendas dos produtos, considerando o total arrecadado das vendas de cada item.
# Faixa dos menores valores de venda;
# Qual valor representa o valor central das vendas;
# A partir de qual faixa estão os produtos com maior representatividade financeira.

import pandas as pd
import numpy as np
import os

os.system('csl')

df_planilha_moveis = pd.read_csv('planilha_moveis.csv')
print(df_planilha_moveis.head())

print('\nDados Obtido')
print(100 * '=')
print(df_planilha_moveis.head())
print(df_planilha_moveis['Total Arrecadado'])

df_planilha_moveis['Total Arrecadado'] = (
    df_planilha_moveis['Vendidos'] *
    df_planilha_moveis['Preço']
)

array_total_vendas = np.array(df_planilha_moveis['Preço Total (R$)'])


print('\nMedidas de Tendência Central')
print(30*"=")
media = np.mean(array_total_vendas)
print(f'\nMédia dos Custos: {media:.2f}')

mediana = np.median(array_total_vendas)
print(f'\nMediana dos Custos: {mediana:.2f}')

q1 = np.quantile(array_total_vendas, 0.25) # 25%
q2 = np.quantile(array_total_vendas, 0.50) # 50%
q3 = np.quantile(array_total_vendas, 0.75) # 75%

print('\nMedidas de Posição')
print(30*"=")
print(f'Q1: {q1}')
print(f'Q2: {q2}')
print(f'Q3: {q3}')
