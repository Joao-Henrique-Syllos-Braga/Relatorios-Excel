import sys
from excel import createExcel

# Verifica se mais de um argumento foi passado (além do script)
if len(sys.argv) > 2:
    arquivo = sys.argv[1]  # Primeiro argumento: arquivo recebido
    local_arq = sys.argv[2]  # Segundo argumento: local do arquivo

    print(f"Arquivo recebido: {arquivo}")
    print(f"Local selecionado: {local_arq}")

    # Chama a função createExcel
    createExcel(arquivo, local_arq)

    print(f"Função executada")
else:
    print("Argumentos insuficientes. Esperados: arquivo e local.")