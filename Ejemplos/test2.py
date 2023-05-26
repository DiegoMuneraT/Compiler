def construir_tabla_ll1(producciones):
    # Paso 1: Obtener los conjuntos FIRST y FOLLOW
    first = obtener_first(producciones)
    follow = obtener_follow(producciones, first)

    # Paso 2: Inicializar la tabla LL(1)
    tabla_ll1 = {}
    for no_terminal in producciones:
        tabla_ll1[no_terminal] = {}

    # Paso 3: Calcular la tabla LL(1)
    for no_terminal in producciones:
        for produccion in producciones[no_terminal]:
            conjunto_first = obtener_first([produccion], first)
            for simbolo in conjunto_first:
                if simbolo != "epsilon":
                    if simbolo in tabla_ll1[no_terminal]:
                        print("La gramática no es LL(1).")
                        return None
                    else:
                        tabla_ll1[no_terminal][simbolo] = produccion

            if "epsilon" in conjunto_first:
                conjunto_follow = follow[no_terminal]
                for simbolo in conjunto_follow:
                    if simbolo in tabla_ll1[no_terminal]:
                        print("La gramática no es LL(1).")
                        return None
                    else:
                        tabla_ll1[no_terminal][simbolo] = produccion

    # Paso 4: Devolver la tabla LL(1)
    return tabla_ll1


def obtener_first(producciones):
    first = {}
    for no_terminal in producciones:
        first[no_terminal] = set()

    for no_terminal in producciones:
        for produccion in producciones[no_terminal]:
            i = 0
            while i < len(produccion):
                if produccion[i] in first:
                    if "epsilon" not in first[produccion[i]]:
                        first[no_terminal] |= first[produccion[i]]
                        break
                    else:
                        first[no_terminal] |= (first[produccion[i]] - set(["epsilon"]))
                        i += 1
                else:
                    first[no_terminal].add(produccion[i])
                    break
            else:
                first[no_terminal].add("epsilon")

    return first


def obtener_follow(producciones, first):
    follow = {}
    for no_terminal in producciones:
        follow[no_terminal] = set()
    
    follow[next(iter(producciones))].add("$")
    
    for no_terminal in producciones:
        for produccion in producciones[no_terminal]:
            for i in range(len(produccion)):
                if produccion[i] in producciones:
                    if i < len(produccion)-1 and produccion[i+1] in first:
                        follow[produccion[i]] |= first[produccion[i+1]] - set(["epsilon"])
                    elif i == len(produccion)-1:
                        follow[produccion[i]] |= follow[no_terminal]
                    j = i+1
                    while j < len(produccion) and "epsilon" in first[produccion[i]]:
                        follow[produccion[i]] |= (first[produccion[j]] - set(["epsilon"]))
                        if j < len(produccion)-1 and produccion[j+1] in first:
                            follow[produccion[i]] |= first[produccion[j+1]] - set(["epsilon"])
                        elif j == len(produccion)-1:
                            follow[produccion[i]] |= follow[no_terminal]
                        j += 1
                        
    return follow



gramatica = {
    'S': [['A', 'B'], ['C', 'D']],
    'A': [['a', 'A'], ['epsilon']],
    'B': [['b', 'B'], ['epsilon']],
    'C': [['c', 'C'], ['epsilon']],
    'D': [['d', 'D'], ['epsilon']],
}

tabla_ll1 = construir_tabla_ll1(gramatica)