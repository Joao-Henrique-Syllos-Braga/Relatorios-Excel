import pandas as pd
from setCLasses import setClasses

def data():
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

        for _, row in df.iterrows():
            # Obtém os valores da linha atual
            classe = row["Classe"]
            valor = row["Valor"]
            comp = row["Competência"]

            # Verifica se a classe corresponde à classe atual
            if classe == newClasse and isinstance(comp, pd.Timestamp):
                mes = comp.month  # Obtém o número do mês (1 a 12)
                if 1 <= mes <= 12 and comp.year == 2024:  # Verifica se o mês é válido
                    valor = round(valor, 2)
                    curret_local[mes - 1] += valor  # Soma o valor no índice correspondente ao mês

        # Adiciona os dados da classe atual à lista geral
        data.append(curret_local)

    # Exibe os dados organizados
    for x in data:
        print(x)

    return data
