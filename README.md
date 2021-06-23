# Compiler
- Team Project of CAUSW 2021 Compiler Class
- Java lexical analyzer and syntax analyzer with Python Code

# Author
<table>
  <tr>
     <td align="center"><a href="https://github.com/Youhoseong"><img src="https://avatars.githubusercontent.com/u/33655186?v=4" width="150px;" alt=""/><br/><sub><b>유호성</b></sub></a></td>
    <td align="center"><a href="https://github.com/quadbeats"><img src="https://avatars.githubusercontent.com/u/33650185?v=4" width="150px;" alt=""/><br/><sub><b>조성규</b></sub></a></td>



  </tr>
</table>
  
# Design Process for lexical analyzer

1. Make Regular Expression for each token
2. Design Non-deterministic Finite Automata(NFA)
3. Convert NFA to DFA
4. Implement using Python

# Design Process for syntax analyzer
1. Make CFG. (It should not be ambiguous.)
2. Make SLR-Table. 
3. Implement using Python

# Using Process
1. clone this repository
```
$ git clone https://github.com/Youhoseong/_lexical_analyzer.git
```
2. Need "codein.java" file as a input descripting any Java Codes.

```java
class CodeIn {
    
    int SILHUM (int SG) {
        int a;
        char b = 'a';
        int c = a + 1;
        int d = a * 3;
        String str = "This is compiler class";

        if ( false < true ) {
            a=b;
        }
        else {
            b=a;
        }

        while(true) {

        }

        return a;
    }
}
```
3. On your terminal, execute.

```
python lexical_analyzer.py codein.java 
```
4. You can see lexical_analyzer result (codeout.txt will be created)

```
<CLASS, class, 1>
<ID, CodeIn, 1>
<LBRACE, {, 1>
<VTYPE, int, 3>
<ID, SILHUM, 3>
<LPAREN, (, 3>
<VTYPE, int, 3>
<ID, SG, 3>
<RPAREN, ), 3>
<LBRACE, {, 3>
<VTYPE, int, 4>
<ID, a, 4>
<SEMI, ;, 4>
<VTYPE, char, 5>
<ID, b, 5>
<OP, =, 5>
<CHAR, a, 5>
<SEMI, ;, 5>
<VTYPE, int, 6>
<ID, c, 6>
<OP, =, 6>
<ID, a, 6>
<OP, +, 6>
<INTEGER, 1, 6>
<SEMI, ;, 6>
<VTYPE, int, 7>
<ID, d, 7>
<OP, =, 7>
<ID, a, 7>
<OP, *, 7>
<INTEGER, 3, 7>
<SEMI, ;, 7>
<VTYPE, String, 8>
<ID, str, 8>
<OP, =, 8>
<STR, This is compiler class, 8>
<SEMI, ;, 8>
<IF, if, 10>
<LPAREN, (, 10>
<FALSE, false, 10>
<OP, <, 10>
<TRUE, true, 10>
<RPAREN, ), 10>
<LBRACE, {, 10>
<ID, a, 11>
<OP, =, 11>
<ID, b, 11>
<SEMI, ;, 11>
<RBRACE, }, 12>
<ELSE, else, 13>
<LBRACE, {, 13>
<ID, b, 14>
<OP, =, 14>
<ID, a, 14>
<RBRACE, }, 15>
<WHILE, while, 17>
<LPAREN, (, 17>
<TRUE, true, 17>
<RPAREN, ), 17>
<LBRACE, {, 17>
<RBRACE, }, 19>
<RETURN, return, 21>
<ID, a, 21>
<SEMI, ;, 21>
<RBRACE, }, 22>
<RBRACE, }, 23>

```


5. On your terminal, execute.

```
python syntax_analyzer.py codeout.txt
```

6. You can see syntax_analyzer result
```
ex)
#######################################

# REJECT, There is Error.
# Reject from Line Number: 14
# Last token of [   b = a   ] is missing.

#######################################
```


# License
MIT License

  
