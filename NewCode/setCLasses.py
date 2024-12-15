import pandas as pd

def setClasses(df):
    classes = []
    for _, row in df.iterrows():
        classe = row["Classe"]
        if classe not in classes:
            classes.append(classe)
        else:
            continue
    classes = [x for x in classes if pd.notna(x)]
    classes.sort()
    return classes