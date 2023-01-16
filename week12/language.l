%{
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int lines = 1;
%}

%option noyywrap
%option caseless

DIGIT [0-9]
NON_ZERO_DIGIT [1-9]
INT_CONSTANT [+-]?{NON_ZERO_DIGIT}{DIGIT}*|0
LETTER [a-zA-Z_]

%%

"array" {printf("ARRAY\n");}
"of" {printf("OF\n");}
"char" {printf("CHAR\n");}
"string" {printf("STRING\n");}
"int" {printf("INT\n");}
"const" {printf("CONST\n");}
"typedef" {printf("TYPEDEF\n");}
"var" {printf("VAR\n");}
"if" {printf("IF\n");}
"else" {printf("ELSE\n");}
"read" {printf("READ\n");}
"write" {printf("WRITE\n");}
"while" {printf("WHILE\n");}
"BEGIN" {printf("BEGIN\n");}
"END" {printf("END\n");}

"+" {printf("ADD\n");}
"-" {printf("SUB\n");}
"*" {printf("MUL\n");}
"/" {printf("DIV\n");}
"%" {printf("MOD\n");}
"=" {printf("ASSIGN\n");}
"==" {printf("EQ\n");}
"!=" {printf("NEQ\n");}
"<" {printf("LT\n");}
"<=" {printf("LEQ\n");}
">" {printf("GT\n");}
">=" {printf("GEQ\n");}

"(" {printf("LPAREN\n");}
")" {printf("RPAREN\n");}
"{" {printf("LBRACE\n");}
"}" {printf("RBRACE\n");}
"[" {printf("LBRACKET\n");}
"]" {printf("RBRACKET\n");}
";" {printf("SEMICOLON\n");}
" " {printf("SPACE\n");}
{INT_CONSTANT} {printf("INTEGER: %s\n", yytext);}
{LETTER}({LETTER}|{DIGIT})* {printf("IDENTIFIER: %s\n", yytext);}
{DIGIT}+{LETTER}+({LETTER}|{DIGIT})* {printf("Error at token %s at line %d\n", yytext, lines); exit(1);}
"\n" {lines++; printf("NEWLINE\n");}
. {printf("Error at token %s at line %d\n", yytext, lines); exit(1);}

%%

int main(int argc, char **argv) {
    FILE *file;

    if (argc > 1) {
        file = fopen(argv[1], "r");
        if (!file) {
            fprintf(stderr, "Could not open file %s\n", argv[1]);
            return 1;
        }
    } else {
        file = stdin;
    }

    yyin = file;
    yylex();
    fclose(file);
    return 0;
}
