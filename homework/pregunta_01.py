"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """

    suma = 0
    with open("files/input/data.csv", "r", encoding="utf-8") as file:
        for line in file:
            # Separamos los campos por tabulación (o coma, según el formato real del CSV)
            # data.csv en este laboratorio suele usar tabulaciones '\t'
            columns = line.strip().split("\t")
            
            # Sumamos el valor de la segunda columna (índice 1) convertido a entero
            suma += int(columns[1])
            
    return suma

if __name__ == "__main__":
    resultado = pregunta_01()
    print(f"El resultado de la suma es: {resultado}")