import pandas as pd

# Carregar os dados
df = pd.read_excel("Arquivo.xlsx", sheet_name=0)

# Substituir valores nulos na coluna 'Valor' por 0
df['Valor'] = df['Valor'].fillna(0)

# Meses
mesList = ["JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"]


#pegar a linha que tem o valor 1.1 V
#pegar o valor da 
total = 0
for index, row in df.iterrows():
    if row["Classe"] == 1.10:
        if isinstance(row["Competência"], pd.Timestamp):
            otherV = row["Competência"]
            if otherV.year == 2024:
                total += row["Valor"]
        else:
            if otherV.year == 2024:
                total += row["Valor"]
        

print(total)