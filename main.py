import pandas as pd

# Carregar os dados
df = pd.read_excel("00-Acompanhamento SAB TECH-OUT 24.xlsx", sheet_name=0)

# Substituir valores nulos na coluna 'Valor' por 0
df['Valor'] = df['Valor'].fillna(0)

# Meses
mesList = ["JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"]

data = [
    ["Meses", "JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC", "Total"],

    ["Receita 1.10", 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0, 0, 0, 0],
    
    [2.01],
    ["Prolabore", 0, 0, 0, 0, 0, 0 ,0 ,0, 0, 0, 0, 0, 0 ],
    ["IRRF/INSS prolabore", 0, 0, 0, 0, 0, 0 ,0 ,0, 0, 0, 0, 0, 0 ],
    ["Retirada Ana Paula Syllos Braga", 0, 0, 0, 0, 0, 0 ,0 ,0, 0, 0, 0, 0, 0 ],
    ["Retirada Sérgio Augusto Braga", 0, 0, 0, 0, 0, 0 ,0 ,0, 0, 0, 0, 0, 0 ],

    [2.03],
    ["Honorários Contabeis", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],

    [2.04, "", "", "", "", "", "", "", "", "", "", "", "", 0],
    ["Material de informatica", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],         #10
    ["Material de escritório", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]           #11
]
#pegar a linha que tem o valor 1.1 V
#pegar o valor da 





# RECEITA ---------------------------------------------------------------------------
def mesReceita(line, row, data):
    data[1][line.month] += row["Valor"]

def totalReceita(df):
    total = 0
    for index, row in df.iterrows():
        if row["Classe"] == 1.1:
            if isinstance(row["Competência"], pd.Timestamp):
                otherV = row["Competência"]
                if otherV.year == 2024:
                    total += row["Valor"]
                    mesReceita(otherV, row, data)

            else:
                print("Valor invalido")
    data[1][13] = total

totalReceita(df)
# RECEITA ---------------------------------------------------------------------------

# PROLABORE -------------------------------------------------------------------------
def totalProlabore(df):
    total = 0
    def mesProlabore(line, row, data, local):
        data[local][line.month] += row["Valor"]

    def prolabore(data):
        total = 0
        for x in range(3, 13):
            data[3][x-2] += data[4][x-2] + data[5][x-2] + data[6][x-2]
            total += data[4][x-2] + data[5][x-2] + data[6][x-2]
        return total


    for index, row in df.iterrows():
        if row["Classe"] == 2.01:
            if isinstance(row["Competência"], pd.Timestamp):
                otherV = row["Competência"]
                if otherV.year == 2024:
                    match row["Descrição"].lower():
                        case "irrf/inss prolabore":
                            mesProlabore(otherV, row, data, 4)
                        case "retirada ana paula syllos braga":
                            mesProlabore(otherV, row, data, 5)
                        case "retirada sérgio augusto braga":
                            mesProlabore(otherV, row, data, 6)
                    prolabore(data)
            else:
                print("Valor invalido")
    data[3][13] = prolabore(data)

    data[4][13] += sum(data[4][1:13])
    data[5][13] += sum(data[5][1:13])
    data[6][13] += sum(data[6][1:13])

totalProlabore(df)
# PROLABORE -------------------------------------------------------------------------

# HONORÁRIOS CONTABEIS --------------------------------------------------------------
def totalHonorario(df):
    def mesHonorario(line, row, data):
        data[8][line.month] += row["Valor"]

    total = 0
    for index, row in df.iterrows():
        if row["Classe"] == 2.03:
            if isinstance(row["Competência"], pd.Timestamp):
                otherV = row["Competência"]
                if otherV.year == 2024:
                    total += row["Valor"]
                    mesHonorario(otherV, row, data)
            else:
                print("Valor invalido")
    data[8][13] = total
totalHonorario(df)
# HONORÁRIOS CONTABEIS --------------------------------------------------------------

# DESPESAS VARIADAS -----------------------------------------------------------------
def mesDespesa(line, row, data, index):
    data[index][line.month] += row["Valor"]
total = 0
for index, row in df.iterrows():
    if row["Classe"] == 2.04:
        if isinstance(row["Competência"], pd.Timestamp):
            otherV = row["Competência"]
            if otherV.year == 2024:
                total += row["Valor"]
                match row["Descrição"].lower():
                    case "material de escritório":
                        mesDespesa(otherV, row, data, 11)
                    case "material de informatica":
                        mesDespesa(otherV, row, data, 10)

data[9][13] = total
data[10][13] = sum(data[10][1:13])
data[11][13] += sum(data[11][1:13])

# DESPESAS VARIADAS -----------------------------------------------------------------
for x in data:
    print("\n", x)