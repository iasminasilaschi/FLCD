%{
#include <stdio.h>
#include <stdlib.h>

int yyerror(char *s);

#define YYDEBUG 1
%}

%token VAR
%token CONST
%token TYPEDEF
%token INT
%token CHAR
%token STRING
%token INTEGER
%token BEGIN
%token END
%token ARRAY
%token OF
%token IDENTIFIER
%token INT_CONSTANT
%token CHARACTER
%token STRING_CONSTANT
%token IF
%token THEN
%token ELSE
%token READ
%token WRITE
%token WHILE
%token BEGIN_PROGRAM
%token END_PROGRAM
%token ADD
%token SUB
%token MUL
%token DIV
%token MOD
%token EQ
%token NEQ
%token LT
%token LEQ
%token GT
%token GEQ
%token LPAREN
%token RPAREN
%token LBRACE
%token RBRACE
%token LBRACKET
%token RBRACKET
%token SEMICOLON
%token SPACE
%token NEWLINE

%start program

%%

program: BEGIN_PROGRAM decllist ';' cmpdstmt END_PROGRAM {printf("valid program\n");}

decllist: declaration {printf("valid declaration list\n");}
        | declaration ';' decllist {printf("valid declaration list\n");}

declaration: type IDENTIFIER {printf("valid declaration\n");}

type: INT {printf("valid type\n");}
    | CHAR {printf("valid type\n");}
    | ARRAY '[' INT_CONSTANT ']' OF type {printf("valid array type\n");}
    | TYPEDEF IDENTIFIER '{' decllist '}' {printf("valid user-defined type\n");}

cmpdstmt: '{' stmtlist '}' {printf("valid compound statement\n");}

stmtlist: stmt {printf("valid statement list\n");}
        | stmt ';' stmtlist {printf("valid statement list\n");}

stmt: simplstmt {printf("valid simple statement\n");}
    | structstmt {printf("valid structured statement\n");}

simplstmt: assignstmt {printf("valid assignment statement\n");}
        | iostmt {printf("valid input/output statement\n");}

assignstmt: IDENTIFIER EQ expression {printf("valid assignment\n");}

expression: expression ADD term {printf("valid expression\n");}
        | expression SUB term {printf("valid expression\n");}
        | term {printf("valid expression\n");}

term: term MUL factor {printf("valid term\n");}
    | term DIV factor {printf("valid term\n");}
    | factor {printf("valid term\n");}

factor: LPAREN expression RPAREN {printf("valid factor\n");}
      | IDENTIFIER {printf("valid factor\n");}
      | INT_CONSTANT {printf("valid factor\n");}
      | CHARACTER {printf("valid factor\n");}
      | STRING_CONSTANT {printf("valid factor\n");}

iostmt: READ IDENTIFIER {printf("valid read statement\n");}
      | WRITE IDENTIFIER {printf("valid write statement\n");}

structstmt: cmpdstmt {printf("valid compound statement\n");}
        | ifstmt {printf("valid if statement\n");}
        | whilestmt {printf("valid while statement\n");}

ifstmt: IF '(' condition ')' THEN stmt ELSE stmt {printf("valid if statement\n");}

whilestmt: WHILE '(' condition ')' cmpdstmt {printf("valid while statement\n");}

condition: expression relop expression {printf("valid condition\n");}

relop: EQ {printf("valid relational operator\n");}
    | NEQ {printf("valid relational operator\n");}
    | LT {printf("valid relational operator\n");}
    | LEQ {printf("valid relational operator\n");}
    | GT {printf("valid relational operator\n");}
    | GEQ {printf("valid relational operator\n");}

%%

int yyerror(char *s) {
    printf("error: %s\n", s);
    return 0;
}

int main() {
    yyparse();
    return 0;
}

