import re

# Funcion para obtener los simbolos de la produccion
def obtener_simbolos(produccion):
    return re.findall('[A-Za-z0-0]+', produccion)

# Funcion para obtener los conjuntos FIRST de un no terminal
def obtener_first(simbolo, producciones, first):
    if simbolo in first:
        return first[simbolo]
    else:
        first[simbolo] = set()
        for produccion in producciones[simbolo]:
            simbolos = obtener_simbolos(produccion)
            if simbolos[0] == simbolo:
                continue
            elif simbolos[0].islower():
                first[simbolo].add(simbolos[0])
            else:
                first[simbolo] |= obtener_first(simbolos[0], producciones, first)
        return first[simbolo]
    
# Función para obtener los conjuntos FOLLOW de un símbolo no terminal
def obtener_follow(simbolo, producciones, first, follow):
    if simbolo in follow:
        return follow[simbolo]
    else:
        follow[simbolo] = set()
        if simbolo == 'S':
            follow[simbolo].add('$')
        for simbolo_en_produccion in producciones:
            for produccion in producciones[simbolo_en_produccion]:
                simbolos = obtener_simbolos(produccion)
                if simbolo not in simbolos:
                    continue
                i = simbolos.index(simbolo)
                if i == len(simbolos) - 1:
                    follow[simbolo] |= obtener_follow(simbolo_en_produccion, producciones, first, follow)
                else:
                    conjunto_first = obtener_first(simbolos[i + 1], producciones, first) - set(['epsilon'])
                    follow[simbolo] |= conjunto_first
                    if 'epsilon' in conjunto_first:
                        follow[simbolo] |= obtener_follow(simbolo_en_produccion, producciones, first, follow)
        return follow[simbolo]
    
# Función para construir la tabla de análisis sintáctico LL(1)
def construir_tabla_ll1(producciones, first, follow):
    tabla_ll1 = {}
    for simbolo_en_produccion in producciones:
        for produccion in producciones[simbolo_en_produccion]:
            print(producciones)
            conjunto_first = obtener_first(produccion[0], producciones, first)
            if 'epsilon' in conjunto_first:
                conjunto_follow = obtener_follow(simbolo_en_produccion, producciones, first, follow)
                conjunto_first -= set(['epsilon'])
                for simbolo in conjunto_follow:
                    if simbolo in tabla_ll1.setdefault(simbolo_en_produccion, {}):
                        print("La gramática no es LL(1)")
                        return None
                    tabla_ll1[simbolo_en_produccion][simbolo] = produccion
            else:
                for simbolo in conjunto_first:
                    if simbolo in tabla_ll1.setdefault(simbolo_en_produccion, {}):
                        print("La gramática no es LL(1)")
                        return None
                    tabla_ll1[simbolo_en_produccion][simbolo] = produccion
    return tabla_ll1

# Función para obtener el conjunto FIRST de cada símbolo no terminal en la gramática
def obtener_first_gramatica(gramatica):
    # Inicializamos el conjunto FIRST de cada símbolo no terminal como un conjunto vacío
    first = {simbolo_no_terminal: set() for simbolo_no_terminal in gramatica}

    # Iteramos sobre cada símbolo no terminal en la gramática
    for simbolo_no_terminal in gramatica:
        obtener_first(simbolo_no_terminal, gramatica, first)

    return first

# Función para obtener el conjunto FOLLOW de cada símbolo no terminal en la gramática
def obtener_follow_gramatica(gramatica):
    # Obtenemos el conjunto FIRST de cada símbolo no terminal en la gramática
    first = obtener_first_gramatica(gramatica)

    # Inicializamos el conjunto FOLLOW de cada símbolo no terminal como un conjunto vacío
    follow = {simbolo_no_terminal: set() for simbolo_no_terminal in gramatica}

    # Agregamos el símbolo de fin de entrada al conjunto FOLLOW de S
    follow['S'] |= set(['$'])

    # Iteramos sobre cada símbolo no terminal en la gramática
    for simbolo_no_terminal in gramatica:
        obtener_follow(simbolo_no_terminal, gramatica, first, follow)

    return follow


"""
Para una gramatica como por ejemplo:
S -> AB | CD
A -> aA | epsilon
B -> bB | epsilon
C -> cC | epsilon
D -> dD | epsilon

Recordar que para que sea LL(1) no puede:
1. Ser ambigua
2. Tener recursion izquierda
"""
#La podemos procesar como un diccionario así:
gramatica = {
    'S': [['A', 'B'], ['C', 'D']],
    'A': [['a', 'A'], ['epsilon']],
    'B': [['b', 'B'], ['epsilon']],
    'C': [['c', 'C'], ['epsilon']],
    'D': [['d', 'D'], ['epsilon']],
}

first = obtener_first_gramatica(gramatica)
follow = obtener_follow_gramatica(gramatica)
tabla = construir_tabla_ll1(gramatica, first, follow)


