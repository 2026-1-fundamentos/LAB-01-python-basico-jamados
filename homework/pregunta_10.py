"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la
    columna 1 y la cantidad de elementos de las columnas 4 y 5.

    Rta/
    [('E', 3, 5),
     ('A', 3, 4),
     ...
     ('E', 2, 3),
     ('E', 3, 3)]


    """
def pregunta_10():
    resultado = []
    
    with open("files/input/data.csv", "r", encoding="utf-8") as file:
        for line in file:
            columns = line.strip().split("\t")
            letra = columns[0]      # Columna 1 (índice 0)
            columna_4 = columns[3]  # Columna 4 (índice 3), ej: "b,g,f"
            columna_5 = columns[4]  # Columna 5 (índice 4), ej: "jjj:12,bbb:2"
            
            # Contamos los elementos de la columna 4 separando por comas
            # "b,g,f".split(",") -> ['b', 'g', 'f'] -> len() es 3
            cant_col_4 = len(columna_4.split(","))
            
            # Contamos los elementos de la columna 5 de la misma forma
            # "jjj:12,bbb:2".split(",") -> ['jjj:12', 'bbb:2'] -> len() es 2
            cant_col_5 = len(columna_5.split(","))
            
            # Guardamos la tupla con la letra y los dos conteos en el orden original del archivo
            resultado.append((letra, cant_col_4, cant_col_5))
            
    return resultado

if __name__ == "__main__":
    # Imprimimos los elementos para verificar con la respuesta muestra
    print(pregunta_10())
