# lexical_analyzer

- First Team Project of CAUSW 2021 Compiler Class
- Java lexical analyzer for Java Syntax Analyzer


# Author
- Hoseong You, CAU
- Sungkyu Cho, CAU
  


# Design Process

1. Make Regular Expression for each token
2. Design Non-deterministic Finite Automata(NFA)
3. Convert NFA to DFA
4. Implement using Python


# Using Process
1. clone this repository
```
$ git clone https://github.com/Youhoseong/_lexical_analyzer.git
```
2. Need "codein.java" file as a input descripting any Java Codes.

```java
public class Codein {
    public static void main(String args[]) {
        char a = '1';
        char b = 'y';
        int x = a + b;
        int[] array = {56, 14};
        boolean bo = false;
        String str = "this is string";

        int _testvar123 = 0;

        if(x >= 12) {
            b = '2';
        }
        else if(x != 15){
            b = '3';
        }
        else {
            b = a / 3;
        }

        while(true) {

        }
    
        return 0;
    }


}
```
3. On your terminal, execute.

```
python lexical_analyzer.py codein.java 
```


# License
MIT License

  