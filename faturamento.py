"""
Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
• O menor valor de faturamento ocorrido em um dia do mês;
• O maior valor de faturamento ocorrido em um dia do mês;
• Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.
"""


import json
with open('dados.json') as json_file:
    dados = json.load(json_file)
print(dados)
# pega o primeiro dado do vetor
primeiro = dados[0]
aux_menor= primeiro['valor']

# busca o menor valor da lista
for dado in dados:
    if dado['valor'] != 0:
        menor = dado['valor']
        if menor < aux_menor:
            aux_menor = menor
print(f'O menor valor de faturamento ocorrido em um dia do mês: {aux_menor}')

# busca p maior valor da lista
aux_maior = primeiro['valor']
for dado in dados:
    if dado['valor'] != 0:
        maior = dado['valor']
        if maior > aux_maior:
            aux_maior = maior
print(f'O maior valor de faturamento ocorrido em um dia do mês: {aux_maior}')

# dias superior a media mensal
soma = 0
media = 0
dias = 0
day_off = 0
for dado in dados:
    if dado['valor'] == 0:
        day_off += 1
    valor = dado['valor']
    soma += valor
    media = soma / (len(dados)-day_off)
for dado in dados:
    if dado['valor'] != 0:
        if dado['valor'] < media:
            dias += 1
print(f'Número de dias no mês em que o valor de faturamento diário foi superior à média mensal: {dias}')


