%{
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "topdown.tab.h"
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
    return 0;
}