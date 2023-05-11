#define SYMBOL 256
#define COLON 257
#define SEMICOLON 258
#define PIPE 259
#define ARROW 260
#define LPAREN 261
#define RPAREN 262
#define LBRACKET 263
#define RBRACKET 264
#define LBRACE 265
#define RBRACE 266
#define ERROR 267

extern int parse_table[256][256];
extern int lhs[];
extern char* rules[];
