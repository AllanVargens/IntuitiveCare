import re

def buscar(input, lista_busca):
    resultados = []
    regex = re.compile(input, re.IGNORECASE)
    for item in lista_busca:
        if re.search(regex, str(item.values())):
            resultados.append(item)
    return resultados

