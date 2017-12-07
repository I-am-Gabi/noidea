#!/usr/bin/env python
# -*- coding: utf-8 -*-

csv_enem = "data/Dados_Enem.csv"
csv_academico = "data/Dados_Cotas.csv"
csv_cep = "data/Dados_cep.csv"


import pandas as pd


# leitura dos arquivos
data_enem = pd.read_csv(csv_enem)
data_academico = pd.read_csv(csv_academico)
data_cep = pd.read_csv(csv_cep)

# remoção da coluna sem nome
data_academico.drop(['Unnamed: 10', 'unidade', 'nota', 'reposicao', 'faltas_unidade'], axis=1, inplace=True)
# remoção da coluna de cep
data_enem.drop(['cep'], axis=1, inplace=True)
#
data_cep.drop(['ano_ingresso'], axis=1, inplace=True)

# merge das duas tabelas
result = pd.merge(data_enem, data_academico, on=['id_discente', 'sexo', 'cotista', 'nota_enem'])
#print(result.head)

#print(type(data_cep))
#print(type(result))
#result = pd.merge(result, data_cep, on=['id_discente', 'sexo', 'cotista'])


# arquivo com resultado final do merge
result.to_csv('data/final-data.csv')