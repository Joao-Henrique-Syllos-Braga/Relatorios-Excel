import pandas as pd

# Carregar os dados
df = pd.read_excel("Arquivo.xlsx", sheet_name=0)

# Substituir valores nulos na coluna 'Valor' por 0
df['Valor'] = df['Valor'].fillna(0)

# Inicializa listas para armazenar os valores por ano
dataSum23 = []
dataSum24 = []

# Meses
mesList = ["JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"]

# Inicializa dicionários para armazenar os valores por mês e ano (sem somar, apenas armazenar)
mesesSum23 = {mes: [] for mes in mesList}
mesesSum24 = {mes: [] for mes in mesList}

# Função para processar a competência e retornar ano e mês
def processar_competencia(x):
    if isinstance(x, pd.Timestamp):  # Verifica se é um Timestamp
        x = x.strftime('%b-%y')  # Formato: 'Sep-23', 'Oct-24', etc.
    return x.upper().split("-")  # Converte para maiúsculas e separa

# Iterando sobre as linhas do DataFrame com iterrows()
for index, row in df.iterrows():
    # Processa a competência
    competencia = row['Competência']
    temp = processar_competencia(competencia)
    
    if len(temp) == 2:  # Verifica se a competência foi formatada corretamente
        ano = temp[1]  # Ano está no segundo índice (index 1)
        mes = temp[0]

        # Adiciona o valor na lista correspondente ao ano e mês
        if ano == "23":
            dataSum23.append(row["Valor"])
            if mes in mesesSum23:
                mesesSum23[mes].append(row["Valor"])  # Adiciona o valor na lista de meses de 2023
        elif ano == "24":
            dataSum24.append(row["Valor"])
            if mes in mesesSum24:
                mesesSum24[mes].append(row["Valor"])  # Adiciona o valor na lista de meses de 2024
        else:
            print(f"Ano inválido na competência {competencia}")

    else:
        print(f"Competência inválida: {competencia}")

# Cálculo dos totais (soma de valores)
total23 = sum(dataSum23)
total24 = sum(dataSum24)

# Exibe os totais por ano
print("Total 2023:", total23)
print("Total 2024:", total24)

# Exibe os valores por mês para 2023 e 2024
print("Valores por mês (2023):")
for mes, valores in mesesSum23.items():
    print(f"{mes}: {valores}")

print("\nValores por mês (2024):")
for mes, valores in mesesSum24.items():
    print(f"{mes}: {valores}")
