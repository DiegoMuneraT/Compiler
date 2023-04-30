%{
#include <stdio.h>
#define NUMBER 256
#define IDENTIFIER 257
%}


%%
[0-9]+ {return NUMBER; }
[a-zA-Z0-9]+ {return IDENTIFIER; }
. {return -1;}
%%


int main(){
int token;
while ((token = yylex())){
switch(token){
case NUMBER: printf("NUMBER: %s, LENGTH:%d\n", yytext, yyleng); break;
case IDENTIFIER: printf("IDENTIFIER: %s, LENGTH:%d\n", yytext, yyleng); break;
default: printf("Error: %s not recognized\n", yytext);
}
}
}