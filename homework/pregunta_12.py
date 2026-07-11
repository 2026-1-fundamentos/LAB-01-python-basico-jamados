"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

    """
    sumas_por_letra = {}
    
    with open("files/input/data.csv", "r", encoding="utf-8") as file:
        for line in file:
            columns = line.strip().split("\t")
            letra_principal = columns[0]  # Columna 1 (índice 0)
            columna_5 = columns[4]        # Columna 5 (índice 4), ej: "jjj:12,bbb:2"
            
            # 1. Separamos las parejas de la columna 5 por sus comas
            parejas = columna_5.split(",")
            
            suma_fila = 0
            # 2. Recorremos cada pareja para extraer solo el número y sumarlo
            for pareja in parejas:
                _, valor_texto = pareja.split(":")
                suma_fila += int(valor_texto)
                
            # 3. Acumulamos la suma total de esta fila en la letra correspondiente
            if letra_principal in sumas_por_letra:
                sumas_por_letra[letra_principal] += suma_fila
            else:
                sumas_por_letra[letra_principal] = suma_fila
                
    # 4. Construimos el diccionario ordenado alfabéticamente
    resultado_ordenado = {}
    for letra in sorted(sumas_por_letra.keys()):
        resultado_ordenado[letra] = sumas_por_letra[letra]
        
    return resultado_ordenado

if __name__ == "__main__":
    print(pregunta_12())
