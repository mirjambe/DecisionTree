import pandas as pd

data = pd.read_csv('Igra.csv', delimiter=";")
print(data)

dataVrijeme = data.groupby(['Vrijeme', 'Igrati?']).groups
print('Vrijeme')
for key in dataVrijeme:
    print(key, "-->", len(dataVrijeme[key]))

dataTemp = data.groupby(['Temperatura', 'Igrati?']).groups
print('Temperatura')
for key in dataTemp:
    print(key, "-->", len(dataTemp[key]))
