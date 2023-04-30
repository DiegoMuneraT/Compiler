# Lenguajes formales y compiladores

## Qué se realizó?

1. Analizador sintactico descendente (Top-Down)
2. Analizador sintactico ascendente (Bottom-Up)

## Input

Una gramatica libre de contexto G. Se recibe una lista de n > 0 cadenas, cada cadena en una linea independiente. La entrada termina cuando se lee una linea en blanco.

## Output

Si no se puede implementar el analizador retornará el mensaje “error”. De lo contrario, por cada cadena de la entrada imprimirá “si”, si la cadena pertenece a L(G), o “no”, si la cadena no pertenece a L(G). Se imprimirá una linea independiente por cada cadena (i.e. deben haber n lineas).

## Ejemplo

### Input
`S -> aSb | c`
`aacbb`
`acb`
`ab`

### Output
`si`
`si`
`no`