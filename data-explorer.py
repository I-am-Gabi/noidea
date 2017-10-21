import pandas as pd

# leitura dos arquivos
data_file = "data/final-data.csv"
data = pd.read_csv(data_file)

# selecionar so os dados dos cotistas
mask = (data['cotista'] == 't')
cotistas = data[mask]

print(cotistas['media_final'].mean())
print(cotistas['media_final'].median())
print(cotistas['media_final'].max())
print(cotistas['media_final'].min())
