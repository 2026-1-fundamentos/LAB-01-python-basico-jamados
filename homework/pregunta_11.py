"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada
    letra de la columna 4, ordenadas alfabeticamente.

    Rta/
    {'a': 122, 'b': 49, 'c': 91, 'd': 73, 'e': 86, 'f': 134, 'g': 35}


    """
    sumas_por_letra = {}
    
    with open("files/input/data.csv", "r", encoding="utf-8") as file:
        for line in file:
            columns = line.strip().split("\t")
            valor = int(columns[1])    # Columna 2 (índice 1)
            columna_4 = columns[3]    # Columna 4 (índice 3), ej: "b,g,f"
            
            # Separamos las letras minúsculas de la columna 4 usando la coma
            letras = columna_4.split(",")
            
            # Recorremos cada letra encontrada en esa fila
            for letra in letras:
                # Le sumamos el valor actual a cada letra de la lista
                if letra in sumas_por_letra:
                    sumas_por_letra[letra] += valor
                else:
                    sumas_por_letra[letra] = valor
                    
    # Construimos el diccionario final ordenado alfabéticamente por sus llaves
    resultado_ordenado = {}
    for letra in sorted(sumas_por_letra.keys()):
        resultado_ordenado[letra] = sumas_por_letra[letra]
        
    return resultado_ordenado

if __name__ == "__main__":
    print(pregunta_11())