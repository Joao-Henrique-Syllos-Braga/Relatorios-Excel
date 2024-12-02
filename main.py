import pandas as pd

# Carregar os dados
df = pd.read_excel("00-Acompanhamento SAB TECH-OUT 24.xlsx", sheet_name=0)

# Substituir valores nulos na coluna 'Valor' por 0
df['Valor'] = df['Valor'].fillna(0)

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

    [2.04, "Despesas", "", "", "", "", "", "", "", "", "", "", "", 0],
    ["Material de informatica", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],         
    ["Material de escritório", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],

    [2.05, "", "", "", "", "", "", "", "", "", "", "", "", 0],
    ["ISS retido", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    ["SIMPLES NACIONAL", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ["Outras taxas e impostos", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],

    [2.06],
    ["Despesa de viagem", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],

    [2.07, "Veiculo", "", "", "", "", "", "", "", "", "", "", "", 0],
    ["Estacionamento", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], #19
    ["Combustivel", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ["Lavagem de carro", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ["Manutenção Veículo", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ["IPVA carro", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ["Pneus", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],

    [2.08],
    ["Alimentação", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],

    [2.09],
    ["Plano de Saúde", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],

    [2.50],
    ["Emprestimos Socios", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],

    [2.52],
    ["Pagamento Sócios", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

def setMonth(comp, row, data, local):
    data[local][comp.month] += row["Valor"]



def totalProlabore(data):
    total = 0
    for x in range(3, 12):
        data[3][x-2] += data[4][x-2] + data[5][x-2] + data[6][x-2]
        total += data[4][x-2] + data[5][x-2] + data[6][x-2]
    return total

def prolabore(data):
    for x in range(3, 13):
        data[3][x-2] += data[4][x-2] + data[5][x-2] + data[6][x-2]

year = 2024

for index, row in df.iterrows():
    classe = row["Classe"]
    comp = row["Competência"]
    if classe == 1.10 and comp.year == year:
        setMonth(comp, row, data, 1)
    elif classe == 2.01 and comp.year == year:
        match row["Descrição"].lower():
            case "irrf/inss prolabore":
                setMonth(comp, row, data, 4)
            case "retirada ana paula syllos braga":
                setMonth(comp, row, data, 5)
            case "retirada sérgio augusto braga":
                setMonth(comp, row, data, 6)
    elif classe == 2.03 and comp.year == year:
        setMonth(comp, row, data, 8)
    elif classe == 2.04 and comp.year == year:
        match str(row["Descrição"]).lower():
            case "material de informatica":
                setMonth(comp, row, data, 10)
            case "material de escritório":
                setMonth(comp, row, data, 11)
    elif classe == 2.05 and comp.year == year:
        match row["Descrição"].lower():
            case "iss retido":
                setMonth(comp, row, data, 13)
            case "simples nacional":
                setMonth(comp, row, data, 14)
            case "outras taxas e impostos":
                setMonth(comp, row, data, 15)
    elif classe == 2.06 and comp.year == year:
        setMonth(comp, row, data, 17)
    elif classe == 2.07 and comp.year == year:
        match row["Descrição"].lower():
            case "estacionamento":
                setMonth(comp, row, data, 19)
            case "combustível":
                setMonth(comp, row, data, 20)
            case "lavagem de carro":
                setMonth(comp, row, data, 21)
            case "manurtenção":
                setMonth(comp, row, data, 22)
            case "manutenção":
                setMonth(comp, row, data, 22)
            case "ipva carro":
                setMonth(comp, row, data, 23)
            case "pneus":
                setMonth(comp, row, data, 24)
    elif classe == 2.08 and comp.year == year:
        setMonth(comp, row, data, 26)
    elif classe == 2.09 and comp.year == year:
        setMonth(comp, row, data, 28)
    elif classe == 2.50 and comp.year == year:
        setMonth(comp, row, data, 30)
    elif classe == 2.51 and comp.year == year:
        setMonth(comp, row, data, 32)
data[1][13] += sum(data[1][1:12])

data[4][13] += sum(data[4][1:12])
data[5][13] += sum(data[5][1:12])
data[6][13] += sum(data[6][1:12])

data[3][13] += totalProlabore(data)

data[8][13] += sum(data[8][1:12])

data[9][13] += sum(data[10][1:12]) + sum(data[11][1:12])
data[10][13] += sum(data[10][1:12])
data[11][13] += sum(data[11][1:12])

data[12][13] += sum(data[13][1:12]) + sum(data[13][1:12]) + sum(data[15][1:12])
data[13][13] += sum(data[13][1:12])
data[14][13] += sum(data[14][1:12])
data[15][13] += sum(data[15][1:12])

data[17][13] += sum(data[17][1:12])

data[18][13] += sum(data[19][1:12]) + sum(data[20][1:12]) + sum(data[21][1:12]) + sum(data[22][1:12]) + sum(data[23][1:12]) + sum(data[24][1:12])
data[19][13] += sum(data[19][1:12])
data[20][13] += sum(data[20][1:12])
data[21][13] += sum(data[21][1:12])
data[22][13] += sum(data[22][1:12])
data[23][13] += sum(data[23][1:12])
data[24][13] += sum(data[24][1:12])

data[26][13] += sum(data[26][1:12])

data[28][13] += sum(data[28][1:12])

data[30][13] += sum(data[30][1:12])

data[32][13] += sum(data[32][1:12])
                          
for x in data:
    print("\n", x)