#!/usr/bin/env python
# -*- coding: utf-8 -*-

csv_enem = "data/Cotas_Bel.csv"
csv_academico = "data/Dados_Cotas.csv"

import pandas as pd


# leitura dos arquivos
data_enem = pd.read_csv(csv_enem)
data_academico = pd.read_csv(csv_academico)

# remoção da coluna sem nome
data_academico.drop(['Unnamed: 10', 'unidade', 'nota', 'reposicao', 'faltas_unidade'], axis=1, inplace=True)

# merge das duas tabelas
result = pd.merge(data_enem, data_academico, on=['id_discente', 'sexo', 'cotista', 'nota_enem'])
print(result.head)

# arquivo com resultado final do merge
result.to_csv('final-data.csv')