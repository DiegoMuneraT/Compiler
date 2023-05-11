%{
#include "topdown.tab.h"
%}

%%
[ \t\n] ; /* Ignorar espacios en blanco y saltos de línea */

[a-zA-Z]+   { yylval = strdup(yytext); return SYMBOL; } /* Terminales */
':'         { return COLON; }
';'         { return SEMICOLON; }
'|'         { return PIPE; }
"->"        { return ARROW; }
'('         { return LPAREN; }
')'         { return RPAREN; }
'['         { return LBRACKET; }
']'         { return RBRACKET; }
'{'         { return LBRACE; }
'}'         { return RBRACE; }

.           { printf("Error de sintaxis: Caracter no reconocido -> '%s'\n", yytext); return ERROR; }

%%

int yywrap() {
    return 1;
}
