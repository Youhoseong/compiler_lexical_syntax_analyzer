/**
 *
 Lexical Analyzer 
 *
 2021 Complier Class,
 Author: Hoseong You, SungKyu Cho
 *
 **/

#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <ctype.h>
#include <stdlib.h>
#include <string.h>
#include <iostream>
 using namespace std;


/* Global Variable */
int nextToken;
int charClass;
char lexeme[100];
char nextChar;
int lexLen;
int token;
int previousToken;


char * input;
char* Keyword_ary[9] = { "int", "char", "boolean", "String", "for", "while", "if","else","do"};
FILE* in_fp;
FILE* out_fp;

/* Local Function declarations */
void addChar();
void getChar();
void getNonBlank();
int lex();

/* Character classes */
#define LETTER 0
#define DIGIT 1
#define UNKNOWN 99

/* Token codes */
#define INT_LIT 10
#define CHAR_LIT 29
#define STR_LIT 30
#define UNALLOWED -999

#define IDENT 11
#define KEYWORD 12
#define SEPARATOR 13

#define ASSIGN_OP 20
#define ADD_OP 21
#define SUB_OP 22
#define MULT_OP 23
#define DIV_OP 24
#define LEFT_PAREN 25
#define RIGHT_PAREN 26

#define COMPARE_OP 27
#define QUOTE 28
#define BLANK 31


/******************************************/
/* main driver                            */
/******************************************/
int main()
{

    
    /* Open the input data file and process its contents */
    if ((in_fp = fopen("code.txt", "r")) == NULL) {
        printf("ERROR - cannot open code.in \n");
    }
    if ((out_fp = fopen("code.out", "w")) == NULL) {
        printf("ERROR - cannot write code.out \n");
    }

    else {
        getChar();
        do {
            lex();
        } while (nextToken != EOF);
    }

    return 0;
}

/******************************************
 * lookup - a function to lookup operators
 * and parentheses and return the token
 ******************************************/
int lookup(char ch) {
    switch (ch) {
    case '(':
        addChar();
        nextToken = LEFT_PAREN;
        break;
    case ')':
        addChar();
        nextToken = RIGHT_PAREN;
        break;
    case '\'':
        addChar();
        nextToken = QUOTE;
        break;  

    case '+':
        addChar();
        nextToken = ADD_OP;
        break;
    case '-':
        addChar();
        nextToken = SUB_OP;
        break;
    case '*':
        addChar();
        nextToken = MULT_OP;
        break;
    case '/':
        addChar();
        nextToken = DIV_OP;
        break;
    case ';':
        addChar();
        nextToken = SEPARATOR;
        break;
    case '=':
        addChar();
        nextToken = ASSIGN_OP;
        break;
    case '<':
        addChar();
        nextToken = COMPARE_OP;
        break;
    case '>':
        addChar();
        nextToken = COMPARE_OP;
        break;
    case '{':
        addChar();
        nextToken = SEPARATOR;
        break;
    case '}':
        addChar();
        nextToken = SEPARATOR;
        break;
    default:
        addChar();
        nextToken = EOF;
        break;
    }
    return nextToken;
}


/**************************************************/
/* addChar - a function to add nextChar to lexeme */
/**************************************************/
void addChar() {
    if (lexLen <= 98) {  // max length of Lexime is 99
        lexeme[lexLen++] = nextChar;
        lexeme[lexLen] = 0; // '\0'
    }
    else {
        printf("Error - lexeme is too long \n");
    }
}

/*****************************************************/
/* getChar - a function to get the next character
          of input and determine its character class */
          /*****************************************************/
void getChar() {
    if ((nextChar = getc(in_fp)) != EOF) {
        if (isalpha(nextChar))
            charClass = LETTER;
        else if (isdigit(nextChar))
            charClass = DIGIT;
        else if(nextChar == '\'' || nextChar == '\"') 
            charClass = QUOTE;
        else
            charClass = UNKNOWN;
    }
    else {
        charClass = EOF;
    }
}

void getNonBlank() {
    while (isspace(nextChar))
        getChar();
}

// blank는 토큰 부여를 해야 할 상황이 있고, 하지 않아야 할 상황이 있음, 그래서 판단하는 함수를 따로 생성한다.
void isSpaceBarBlank() {
    if (nextChar != EOF) {
        if (nextChar ==' ')
            charClass = BLANK;

    }
    
}

/*****************************************************/
/* lex - a simple lexical analyzer for arithmetic
         expressions                                 */
         /*****************************************************/
int lex() {
    lexLen = 0;
    getNonBlank();

    switch (charClass) {
        /* Parse identifiers */
    case LETTER:
        addChar();
        getChar();
        
        while (charClass == LETTER || charClass == DIGIT) {
            addChar();
            getChar();
         
        }

        nextToken = IDENT;

        for (int i = 0; i < 7; i++) { //키워드 length로 수정할 것
            if (strcmp(lexeme, Keyword_ary[i]) == 0) {
                nextToken = KEYWORD;
                break;
            }
        }

       
        break;

        /* Parse integer literals */
    case DIGIT:
        addChar();
        getChar();

        while (charClass == DIGIT) {     
            addChar();
            getChar();
        }
         // 처음이 0이고, len >1 일때
        if(lexeme[0] == '0' && lexLen>1)
            nextToken = UNALLOWED;
        else 
            nextToken = INT_LIT;
        
        break;
    case QUOTE: // 딱 3번의 get만 하면됨.
        addChar();
        getChar();

        //getchar 하고나면 nextChar와 charClass가 변경됨.
        isSpaceBarBlank();
        //스페이바에 의한 공백일 때 charClass가 BLANK로 변함.

        //Case1 : 처음 '가 들어오고 두번째 input이 '일때.
        if(lexeme[0] == '\'') {

            if(nextChar == '\'') {
                addChar();
                getChar(); // 다음 input으로 skip
                break;
            }
            else { // Case2: 처음 '가 들어오고 바로 다음 문자가 '가 아닐때
                if (charClass == DIGIT || charClass == LETTER || charClass == BLANK ) {
                    addChar();
                    getChar();

                    if(nextChar == '\'') {
                        addChar();
                        nextToken = CHAR_LIT;
                        getChar(); // 다음 input으로 skip
                        break;
                    }
                    else {
                        addChar();
                        nextToken = UNALLOWED;
                        cout << "Did you skip \' ? ⇩" << '\n';
                        getChar(); // 다음 input으로 skip
                        break;
                    }
                }

            } 
        }
        else { // 큰 따옴표, string error를 어떻게 탐지? => 큰 따옴표 짝이 안맞을 때. 아직 해결x
            while (charClass == LETTER || charClass == DIGIT || charClass == BLANK) {
                addChar();
                getChar();
                isSpaceBarBlank();

                if (nextChar=='\"') {
                    addChar();
                    nextToken = STR_LIT;
                    getChar();
                    
                    break;
                }
         
            }          
        }
        break;
    case UNKNOWN:

        previousToken = nextToken; 

        lookup(nextChar);
        getChar();
      
        if(previousToken == INT_LIT && nextToken== SUB_OP) {
            if (nextChar == DIGIT)
                break;

        }
     
        
        else {
            if(lexeme[0] == '-') {
                while (charClass == DIGIT) {     
                    addChar();
                    getChar();
                }
                if(lexLen > 1)
                    nextToken = INT_LIT;
            }
        }
    

        break;

        /* EOF */
    case EOF:
        nextToken = EOF;
        lexeme[0] = 'E';
        lexeme[1] = 'O';
        lexeme[2] = 'F';
        lexeme[3] = 0;
        break;
    } /* End of switch */
   
    printf("Next token is: %d, Next lexeme is %s\n", nextToken, lexeme);
    return nextToken;
} /* End of function lex */