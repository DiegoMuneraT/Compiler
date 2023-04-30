# Lenguajes formales y compiladores

## Qué se realizó?

1. Analizador sintactico descendente (Top-Down)
2. Analizador sintactico ascendente (Bottom-Up)

## Cómo es su flujo de trabajo?

<img width="758" alt="Captura de pantalla 2023-04-29 a la(s) 11 01 28 p m" src="https://user-images.githubusercontent.com/73514009/235334938-1e745904-001f-4ed0-971d-2c3e3cf4e5e8.png">

## Es posible que se utilice Lex/Flex con Yacc/Bison modificando el proceso así:

<img width="850" alt="Captura de pantalla 2023-04-29 a la(s) 11 08 08 p m" src="https://user-images.githubusercontent.com/73514009/235335081-68e5de7e-76d4-4c8d-8f0a-520d08d9d642.png">

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
