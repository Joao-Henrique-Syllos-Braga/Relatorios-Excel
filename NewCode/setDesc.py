import pandas as pd

from setCLasses import setClasses

# Carregando o arquivo Excel
df = pd.read_excel("arquivo.xlsx")
data = []


# Listas de classes e meses
classes = setClasses(df)  # Recebe uma lista com todas as classes existentes

months = ["January", "February", "March", "April", "May", "June", "July", "August",
          "September", "October", "November", "December"]

for newClasse in classes:
    # Inicializa os valores mensais para a classe atual
    curret_local = [0] * 12  # Lista de 12 zeros (um para cada mês)
    lista_items = []

    for _, row in df.iterrows():
        # Obtém os valores da linha atual
        classe = row["Classe"]
        valor = row["Valor"]
        comp = row["Competência"]
        desc = row["Descrição"]


        if desc not in lista_items:
            print("Valor não encontrado")
            lista_items.append(desc)
        else:
            print("valor encontrado")


    # Criar um local onde será adicionado as listas



    # Adiciona os dados da classe atual à lista geral
    data.append(curret_local)

# Exibe os dados organizados
for x in data:
    print(x)


