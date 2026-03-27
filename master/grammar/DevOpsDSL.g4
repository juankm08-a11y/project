grammar DevOpsDSL;

// ===== PARSER RULES =====

program: statement* EOF;

statement
    : nodeCommand SEMICOLON
    | groupCommand SEMICOLON
    | deployCommand SEMICOLON
    | rule SEMICOLON
    | parallelBlock
    ;

nodeCommand
    : ID PUNTO RUN LPAREN STRING RPAREN
    ;

groupCommand
    : ID PUNTO UPDATE LPAREN RPAREN
    ;

deployCommand
    : DEPLOY ID TO ID
    ;

rule
    : condition ARROW action
    ;

condition
    : ID PUNTO ID comparator NUMBER
    ;

action
    : ID LPAREN RPAREN
    | ID PUNTO RUN LPAREN STRING RPAREN
    ;

parallelBlock
    : PARALLEL LBRACE statement+ RBRACE
    ;

comparator
    : MAYORQUE
    | MENORQUE
    | IGUAL
    | MAYORIGUAL
    | MENORIGUAL
    ;

// ===== LEXER RULES =====

RUN: 'run';
UPDATE: 'update';
DEPLOY: 'deploy';
TO: 'to';
PARALLEL: 'parallel';

PUNTO: '.';
LPAREN: '(';
RPAREN: ')';
LBRACE: '{';
RBRACE: '}';

SEMICOLON: ';';
ARROW: '->';

MAYORQUE: '>';
MENORQUE: '<';
IGUAL: '==';
MAYORIGUAL: '>=';
MENORIGUAL: '<=';

ID: [a-zA-Z_][a-zA-Z0-9_]*;
STRING: '"' .*? '"';
NUMBER: [0-9]+;

WS: [ \t\r\n]+ -> skip;