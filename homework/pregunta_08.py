"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla
    contiene  el valor de la segunda columna; la segunda parte de la tupla
    es una lista con las letras (ordenadas y sin repetir letra) de la
    primera  columna que aparecen asociadas a dicho valor de la segunda
    columna.

    Rta/
    [(0, ['C']),
     (1, ['B', 'E']),
     (2, ['A', 'E']),
     (3, ['A', 'B', 'D', 'E']),
     (4, ['B', 'E']),
     (5, ['B', 'C', 'D', 'E']),
     (6, ['A', 'B', 'C', 'E']),
     (7, ['A', 'C', 'D', 'E']),
     (8, ['A', 'B', 'D', 'E']),
     (9, ['A', 'B', 'C', 'E'])]

    """
    letras_por_numero = {}
    
    with open("files/input/data.csv", "r", encoding="utf-8") as file:
        for line in file:
            columns = line.strip().split("\t")
            letra = columns[0]         # Columna 1
            numero = int(columns[1])   # Columna 2
            
            # Si el número ya existe, añadimos la letra al conjunto (.add)
            # Si no, creamos un conjunto nuevo con esa letra: {letra}
            if numero in letras_por_numero:
                letras_por_numero[numero].add(letra)
            else:
                letras_por_numero[numero] = {letra}
                
    resultado = []
    # Recorremos los números ordenados de menor a mayor
    for numero in sorted(letras_por_numero.keys()):
        # sorted() toma las letras del conjunto, las ordena alfabéticamente
        # y las convierte automáticamente en una lista normal []
        letras_ordenadas = sorted(list(letras_por_numero[numero]))
        resultado.append((numero, letras_ordenadas))
        
    return resultado

if __name__ == "__main__":
    print(pregunta_08())
