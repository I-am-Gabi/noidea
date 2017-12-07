# encoding=utf8  
import sys  

reload(sys)  
sys.setdefaultencoding('utf8')

## numpy is used for creating fake data
import numpy as np 
import matplotlib as mpl 

## agg backend is used to create plot as a .png file
mpl.use('agg')

import matplotlib.pyplot as plt 
import pandas as pd

def set_box_color(bp, color):
    plt.setp(bp['boxes'], color=color)
    plt.setp(bp['whiskers'], color=color)
    plt.setp(bp['caps'], color=color)
    plt.setp(bp['medians'], color=color)

# leitura dos arquivos
data_file = "data/final-data.csv"
data = pd.read_csv(data_file)

# selecionar so os dados dos cotistas e n cotistas
mask = (data['cotista'] == 't')
cotistas = data[mask]

mask = (data['cotista'] == 'f')
nao_cotistas = data[mask]


################ Create a figure instance
fig = plt.figure()
# Create an axes instance
ax = fig.add_subplot(111)

box1 = plt.boxplot([cotistas['nota_enem'], nao_cotistas['nota_enem']], notch=True, patch_artist=True)

ax.set_xticklabels(['Cotistas', 'Não Cotista'])

plt.legend()

plt.tight_layout()
plt.savefig("graph/boxplot_nota_enem.png")  
plt.close()


################ Create a figure instance

### OBSERVAR QUE OS VALORES NULOS (INDEFERIDO, TRANCADO, DESISTENCIA, CANCELADO) FORAM DESCONSIDERADOS

fig = plt.figure()
# Create an axes instance
ax = fig.add_subplot(111)

box1 = plt.boxplot([cotistas['media_final'].dropna(), nao_cotistas['media_final'].dropna()], notch=True, patch_artist=True)

ax.set_xticklabels(['Cotistas', 'Não Cotista'])

plt.legend()

plt.tight_layout()
plt.savefig("graph/boxplot_media_final.png")  
plt.close()


################ Create a figure instance

### OBSERVAR QUE OS VALORES NULOS (INDEFERIDO, TRANCADO, DESISTENCIA, CANCELADO) FORAM DESCONSIDERADOS

fig = plt.figure()
# Create an axes instance
ax = fig.add_subplot(111)
 
box1 = plt.boxplot([cotistas['numero_total_faltas'].dropna(), nao_cotistas['numero_total_faltas'].dropna()], notch=True, patch_artist=True)

ax.set_xticklabels(['Cotistas', 'Não Cotista'])

plt.legend()

plt.tight_layout()
plt.savefig("graph/boxplot_numero_total_faltas.png")  
plt.close()