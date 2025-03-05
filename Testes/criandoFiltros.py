lista = ["aba", "cbc", "aca", "acb"]
listaFiltros = []
parametros = {}

def retornandoUmaListaNovaDeFiltros(lista, opcao):
    listaFiltros = []
    parametros = {}

    for x in lista:
        ultimaLetra = x[-1]  # Pegando a última letra diretamente

        if ultimaLetra in parametros:
            print(f"Adicionando {x} aos parâmetros na chave '{ultimaLetra}'")
            parametros[ultimaLetra].append(x)
        else:
            print(f"Nova chave '{ultimaLetra}', criando lista...")
            parametros[ultimaLetra] = [x]  # Inicializando a lista com o primeiro valor
            listaFiltros.append(ultimaLetra)

    print(parametros)

    # Retornar apenas a lista de filtros
    if opcao == 1:
        return listaFiltros
    # Retornar lista e dicionario de parametros
    elif opcao == 2:
        return listaFiltros, parametros
        
    return Filtros