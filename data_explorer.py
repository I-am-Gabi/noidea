#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encoding=utf8  
import sys  

reload(sys)  
sys.setdefaultencoding('utf8')

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

# leitura dos arquivos
data_file = "data/final-data.csv"
data = pd.read_csv(data_file)

# selecionar so os dados dos cotistas e n cotistas
mask = (data['cotista'] == 't')
cotistas = data[mask]

mask = (data['cotista'] == 'f')
nao_cotistas = data[mask]

# data to plot
situacao_cotistas = cotistas.groupby(["situacao"]).size()
situacao_nao_cotistas = nao_cotistas.groupby(["situacao"]).size()
n_groups = len(situacao_cotistas.index)

################ create plot bat
fig, ax = plt.subplots()
index = np.arange(n_groups)
bar_width = 0.35
opacity = 0.8

rects1 = plt.bar(index, situacao_cotistas, bar_width,
                 alpha=opacity,
                 color='b',
                 label='Cotistas')

rects2 = plt.bar(index + bar_width, situacao_nao_cotistas, bar_width,
                 alpha=opacity,
                 color='g',
                 label='Não Cotistas')             

plt.xlabel('Situação')
plt.ylabel('Ocorrência')
plt.title('Situações Acadêmicas de Cotistas e Não Cotistas')
plt.xticks(index + bar_width, situacao_cotistas.index, rotation='vertical')
plt.legend()
 
plt.tight_layout() 

plt.savefig('graph/situacao.png')
plt.close()

################ create plot circle

dados_cotistas = "{0:.2f}".format(cotistas['media_final'].mean())
dados_nao_cotistas = "{0:.2f}".format(nao_cotistas['media_final'].mean()) 
# create plot
 
# The slices will be ordered and plotted counter-clockwise.
labels = "Cotistas", "Não Cotistas"
values = [dados_cotistas, dados_nao_cotistas]
colors = ['yellowgreen', 'gold']
explode = (0, 0)  # explode a slice if required

plt.pie(values, explode=explode, labels=values, colors=colors, shadow=True)
        
#draw a circle at the center of pie to make it look like a donut
centre_circle = plt.Circle((0,0), 0.75, color='black', fc='white', linewidth=1.25)
fig = plt.gcf()
fig.gca().add_artist(centre_circle)
fig.gca().title.set_position([.5, 1.05])


# Set aspect ratio to be equal so that pie is drawn as a circle.
plt.axis('equal')
plt.title("Média Final")
plt.legend(labels,loc=2)
plt.savefig("graph/media_final.png")  
plt.close()

################ create plot circle

dados_cotistas = "{0:.2f}".format(cotistas['numero_total_faltas'].mean())
dados_nao_cotistas = "{0:.2f}".format(nao_cotistas['numero_total_faltas'].mean())

# create plot
 
# The slices will be ordered and plotted counter-clockwise.
labels = "Cotistas", "Não Cotistas"
values = [dados_cotistas, dados_nao_cotistas]
colors = ['yellowgreen', 'gold']
explode = (0, 0)  # explode a slice if required

plt.pie(values, explode=explode, labels=values, colors=colors, shadow=True)

        
#draw a circle at the center of pie to make it look like a donut
centre_circle = plt.Circle((0,0), 0.75, color='black', fc='white', linewidth=1.25)
fig = plt.gcf()
fig.gca().add_artist(centre_circle)
fig.gca().title.set_position([.5, 1.05])

# Set aspect ratio to be equal so that pie is drawn as a circle.
plt.axis('equal')
plt.title("Número Total de Faltas")
plt.legend(labels,loc=2)
plt.savefig("graph/numero_total_faltas.png")  
plt.close()

################ create plot circle

dados_cotistas = "{0:.2f}".format(cotistas['nota_enem'].mean())
dados_nao_cotistas = "{0:.2f}".format(nao_cotistas['nota_enem'].mean())

# create plot
 
# The slices will be ordered and plotted counter-clockwise.
labels = "Cotistas", "Não Cotistas"
values = [dados_cotistas, dados_nao_cotistas]
colors = ['yellowgreen', 'gold']
explode = (0, 0)  # explode a slice if required

plt.pie(values, explode=explode, labels=values, colors=colors, shadow=True)

#draw a circle at the center of pie to make it look like a donut
centre_circle = plt.Circle((0,0), 0.75, color='black', fc='white', linewidth=1.25)
fig = plt.gcf()
fig.gca().add_artist(centre_circle)
fig.gca().title.set_position([.5, 1.05])

# Set aspect ratio to be equal so that pie is drawn as a circle.
plt.axis('equal')
plt.title("Nota do Enem")
plt.legend(labels,loc=2)
plt.savefig("graph/nota_enem.png")  
plt.close()

