#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd

# leitura dos arquivos
data_file = "data/final-data.csv"
data = pd.read_csv(data_file)

# selecionar so os dados dos cotistas e n cotistas
mask = (data['cotista'] == 't')
cotistas = data[mask]

mask = (data['cotista'] == 'f')
nao_cotistas = data[mask]

print("média: [cotistas = {} ] [ não cotista = {} ]"
      .format(cotistas['media_final'].mean(), nao_cotistas['media_final'].mean()))
print("mediana: [cotistas = {} ] [ não cotista = {} ]"
      .format(cotistas['media_final'].median(), nao_cotistas['media_final'].median()))
print("nota máxima: [cotistas = {} ] [ não cotista = {} ]"
      .format(cotistas['nota_enem'].max(), nao_cotistas['nota_enem'].max()))
print("nota mínima: [cotistas = {} ] [ não cotista = {} ]"
      .format(cotistas['nota_enem'].min(), nao_cotistas['nota_enem'].min()))


print("média nota enem: [cotistas = {} ] [ não cotista = {} ]"
      .format(cotistas['nota_enem'].mean(), nao_cotistas['nota_enem'].mean()))
