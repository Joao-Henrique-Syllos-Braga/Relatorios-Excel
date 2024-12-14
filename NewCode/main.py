import pandas as pd

df = pd.read_excel("arquivo.xlsx")

classes = [1.10, 2.01, 2.02, 2.03, 2.04, 2.05, 2.06, 2.07, 2.09, 2.50, 2.51, 2.60]
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

def convertMes(mes):
    meses = {
        1: "January", 2: "February", 3: "March", 4: "April", 5: "May",
        6: "June", 7: "July", 8: "August", 9: "September", 10: "October",
        11: "November", 12: "December"
    }
    return meses.get(mes, "Mês inválido")



# Exibindo a lista
print(months)

dicClass = {
    "January": [],
    "February": [],
    "March": [],
    "April": [],
    "May": [],
    "June": [],
    "July": [],
    "August": [],
    "September": [],
    "October": [],
    "November": [],
    "December": []
}

# Exibindo o dicionário
print(dicClass)


for _,row in df.iterrows():
    classe = row["Classe"]
    valor = row["Valor"]
    comp = row["Competência"]

    for clas in classes:
        if clas == classe:
            for mes in months:
                curretMonth = convertMes(comp.month)
                if curretMonth == mes:
                    dicClass[mes].append(valor)
                    print(valor)

for x, y in dicClass.items():
    print(f"{x} : {dicClass[x]}")