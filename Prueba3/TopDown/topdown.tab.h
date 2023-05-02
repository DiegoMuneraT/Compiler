#define SYMBOL 257
#define COLON 258
#define SEMICOLON 259
#define PIPE 260
#define ARROW 261
#define LPAREN 262
#define RPAREN 263
#define LBRACKET 264
#define RBRACKET 265
#define LBRACE 266
#define RBRACE 267
#define ERROR 268

extern int yyparse();
extern int yylex();
extern void yyerror(char*);
extern char* yytext;
extern int yylval;
