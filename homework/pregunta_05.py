"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """
    valores_por_letra = {}
    
    with open("files/input/data.csv", "r", encoding="utf-8") as file:
        for line in file:
            columns = line.strip().split("\t")
            letra = columns[0]
            valor = int(columns[1])
            
            # Si la letra ya existe, guardamos el valor en su lista
            # Si no existe, creamos una lista nueva con este primer valor
            if letra in valores_por_letra:
                valores_por_letra[letra].append(valor)
            else:
                valores_por_letra[letra] = [valor]
                
    resultado = []
    # Recorremos el diccionario ordenado alfabéticamente por sus llaves
    for letra in sorted(valores_por_letra.keys()):
        lista_valores = valores_por_letra[letra]
        # max() y min() extraen los extremos de la lista de números
        maximo = max(lista_valores)
        minimo = min(lista_valores)
        resultado.append((letra, maximo, minimo))
        
    return resultado

if __name__ == "__main__":
    print(pregunta_05())
