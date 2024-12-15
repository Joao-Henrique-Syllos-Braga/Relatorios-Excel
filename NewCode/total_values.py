
def totalData(data):
    def soma(lista):
        total = 0
        for x in lista:
            if type(x) != str and x is not None:
                total += x
        return total

    for x in data:
        total = soma(x)
        x.insert(len(x), total)
