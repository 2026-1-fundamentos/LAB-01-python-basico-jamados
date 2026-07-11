"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como
    la lista de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [('A', 8), ('B', 7), ('C', 5), ('D', 6), ('E', 14)]

    """
    conteo = {}
    
    with open("files/input/data.csv", "r", encoding="utf-8") as file:
        for line in file:
            columns = line.strip().split("\t")
            letra = columns[0]  # La primera columna es el índice 0
            
            # Si la letra ya está en el diccionario, sumamos 1.
            # Si no está, la creamos con valor inicial de 1.
            if letra in conteo:
                conteo[letra] += 1
            else:
                conteo[letra] = 1
                
    # conteo.items() convierte el diccionario en una lista de tuplas dict_items([('A', 8), ...])
    # sorted(...) se encarga de ordenarlas alfabéticamente por la clave (la letra)
    resultado_ordenado = sorted(conteo.items())
    
    return resultado_ordenado

# Bloque de prueba local
if __name__ == "__main__":
    print(pregunta_02())
