import pandas as pd

def znacajkaDaNe(colName):
    print(colName)
    dataVrijeme = data.groupby(colName).groups
    for key in dataVrijeme:
        print(key)
        da, ne = 0, 0
        for index in list(dataVrijeme[key]):
            if data.values[index, 5] == 'da':
                da += 1
            else:
                ne += 1
        print("da", da)
        print("ne", ne)
    print("***************************")

data = pd.read_csv('Igra.csv', delimiter=";")
print(data)

columns = list(data)
clumns = columns.remove('Dan')
clumns = columns.remove('Igrati?')
print(columns)

for col in columns:
    znacajkaDaNe (col)
