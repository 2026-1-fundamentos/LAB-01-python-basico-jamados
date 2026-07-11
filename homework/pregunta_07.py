"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla
    contiene un valor posible de la columna 2 y una lista con todas las letras
    asociadas (columna 1) a dicho valor de la columna 2.

    Rta/
    [(0, ['C']),
     (1, ['E', 'B', 'E']),
     (2, ['A', 'E']),
     (3, ['A', 'B', 'D', 'E', 'E', 'D']),
     (4, ['E', 'B']),
     (5, ['B', 'C', 'D', 'D', 'E', 'E', 'E']),
     (6, ['C', 'E', 'A', 'B']),
     (7, ['A', 'C', 'E', 'D']),
     (8, ['E', 'D', 'E', 'A', 'B']),
     (9, ['A', 'B', 'E', 'A', 'A', 'C'])]

    """
    letras_por_numero = {}
    
    with open("files/input/data.csv", "r", encoding="utf-8") as file:
        for line in file:
            columns = line.strip().split("\t")
            letra = columns[0]         # Columna 1 (índice 0)
            numero = int(columns[1])   # Columna 2 (índice 1)
            
            # Agrupamos las letras usando el número como clave del diccionario
            if numero in letras_por_numero:
                letras_por_numero[numero].append(letra)
            else:
                letras_por_numero[numero] = [letra]
                
    # Construimos la lista de tuplas ordenada numéricamente por la clave (el número)
    resultado = []
    for numero in sorted(letras_por_numero.keys()):
        resultado.append((numero, letras_por_numero[numero]))
        
    return resultado

if __name__ == "__main__":
    print(pregunta_07())
