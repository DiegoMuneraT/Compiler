%{
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "bottomup.tab.h"
#define STACK_SIZE 1000
#define INPUT_SIZE 1000
%}

%token SYMBOL COLON SEMICOLON PIPE ARROW LPAREN RPAREN LBRACKET RBRACKET LBRACE RBRACE ERROR

%%

grammar : SYMBOL productions       { printf("Gramática ingresada correctamente.\n"); }
        ;

productions : production
            | productions production
            ;

production : SYMBOL COLON expression SEMICOLON
           ;

expression : term
           | term PIPE expression
           ;

term : SYMBOL
     | LPAREN expression RPAREN
     | LBRACKET expression RBRACKET
     | term expression
     ;

%%

void yyerror(char* msg) {
    printf("Error: %s\n", msg);
}

int main() {
    printf("Ingrese una gramática en formato BNF:\n");
    yyparse();
    printf("Ingrese una cadena para analizar:\n");
    char input[INPUT_SIZE];
    fgets(input, INPUT_SIZE, stdin);
    int i = 0, top = 0, stack[STACK_SIZE];
    stack[0] = SYMBOL;
    while (i < strlen(input)) {
        int sym = yylex();
        if (sym == ERROR) {
            printf("Error: no se pudo analizar la entrada.\n");
            return 1;
        }
        if (stack[top] == sym) {
            top--;
            i++;
        } else if (stack[top] < 256) {
            printf("Error de sintaxis: se esperaba '%c' en la entrada.\n", stack[top]);
            return 1;
        } else {
            int row = stack[top] - 256, col = sym - 256;
            if (parse_table[row][col] == -1) {
                printf("Error de sintaxis: no se puede realizar una reducción.\n");
                return 1;
            }
            int rule = parse_table[row][col];
            int len = strlen(rules[rule]) - 2; /* Eliminar el símbolo no terminal y la flecha */
            top -= len;
            stack[top] = lhs[rule];
            int newrow = stack[top - 1] - 256, newcol = stack[top] - 256;
            stack[top] = parse_table[newrow][newcol];
            top++;
        }
    }
    if (stack[top] == SYMBOL) {
        printf("La cadena ingresada es válida.\n");
    } else {
        printf("La cadena ingresada no es válida.\n");
    }
    return 0;
}
