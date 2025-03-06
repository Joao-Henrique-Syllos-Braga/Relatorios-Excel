import pandas as pd 

df = pd.read_excel(r"C:\Users\João\OneDrive\Desktop\Listão\arquivo.xlsx", sheet_name=0)



# Pegando todas as classes e romovendo NaT
listaDeClasses = [row["Classe"] for _, row in df.iterrows() if pd.notna(row["Classe"])]

# Tratando os dados removendo duplicatas e transformando em tupla
listaDeClassesSet = set(listaDeClasses)
listaDeClassesTemp = list(listaDeClassesSet)
listaDeClassesTemp.sort()
listaDeClasses = tuple(listaDeClassesTemp)

print(listaDeClasses)