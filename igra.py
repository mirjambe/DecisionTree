import pandas as pd
import numpy as np

def znacajkaDaNe(colName, S):
    print("\t",colName)
    dataColumn = data.groupby(colName).groups
    ent_att = 0
    for key in dataColumn:
        # print(key)
        da, ne = 0, 0
        ent_temp = 0
        for index in list(dataColumn[key]):
            if data.values[index, 5] == 'da':
                da += 1
            else:
                ne += 1
        sum_da_ne = da + ne
        ent_temp = -da/sum_da_ne * np.log2(da/sum_da_ne) - ne/sum_da_ne * np.log2(ne/sum_da_ne)
        ent_att += (sum_da_ne/S)*ent_temp
        # print("da", da)
        # print("ne", ne)
        # print("Entropy of " + key, "=", ent_temp)
    print("Entropy of " + colName, "=", ent_att)
    print("***************************")
    return ent_att

data = pd.read_csv('Igra.csv', delimiter=";")
print(data)

columns = list(data)
clumns = columns.remove('Dan')
clumns = columns.remove('Igrati?')
print(columns)
da, ne = 0, 0
for var in data.values[:,5]:
    if var == 'da':
        da += 1
    else:
        ne += 1
sum_da_ne = da + ne
ent_S = -da/sum_da_ne * np.log2(da/sum_da_ne) - ne/sum_da_ne * np.log2(ne/sum_da_ne)
print("Ukupna entropija:", ent_S)
for col in columns:
    ent_att = znacajkaDaNe (col, sum_da_ne)
    print("Gain of attribute: " + col, "=", ent_S - ent_att)