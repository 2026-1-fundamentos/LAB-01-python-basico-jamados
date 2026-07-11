"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras
    corresponde a una clave y el valor despues del caracter `:` corresponde al
    valor asociado a la clave. Por cada clave, obtenga el valor asociado mas
    pequeño y el valor asociado mas grande computados sobre todo el archivo.

    Rta/
    [('aaa', 1, 9),
     ('bbb', 1, 9),
     ('ccc', 1, 10),
     ('ddd', 0, 9),
     ('eee', 1, 7),
     ('fff', 0, 9),
     ('ggg', 3, 10),
     ('hhh', 0, 9),
     ('iii', 0, 9),
     ('jjj', 5, 17)]

    """
    valores_por_clave = {}
    
    with open("files/input/data.csv", "r", encoding="utf-8") as file:
        for line in file:
            columns = line.strip().split("\t")
            # La columna 5 es el índice 4. Contiene algo como "aaa:5,bbb:2,ccc:9"
            columna_5 = columns[4]
            
            # 1. Rompemos el texto por las comas para separar cada pareja clave:valor
            # "aaa:5,bbb:2" -> ['aaa:5', 'bbb:2']
            parejas = columna_5.split(",")
            
            for pareja in parejas:
                # 2. Rompemos cada pareja por los dos puntos ':'
                # 'aaa:5' -> ['aaa', '5']
                clave, valor_texto = pareja.split(":")
                valor = int(valor_texto)  # Lo convertimos a número entero
                
                # 3. Guardamos los números en nuestro diccionario agrupados por su clave
                if clave in valores_por_clave:
                    valores_por_clave[clave].append(valor)
                else:
                    valores_por_clave[clave] = [valor]
                    
    # 4. Construimos la lista final con el mínimo y el máximo de cada clave
    resultado = []
    for clave in sorted(valores_por_clave.keys()):
        lista_numeros = valores_por_clave[clave]
        minimo = min(lista_numeros)
        maximo = max(lista_numeros)
        resultado.append((clave, minimo, maximo))
        
    return resultado

if __name__ == "__main__":
    print(pregunta_06())
