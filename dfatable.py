
import string

class TableofDFA:
    table = {}
    def __init__(self):
        DIGIT_WITHOUT_ZERO = string.digits[1:]
        DIGIT = string.digits
        LETTER = string.ascii_letters
        SPACE = string.whitespace

        self.table = {

            "WHITE_SPACE": {
                0: {
                    SPACE: 1
                },
                1: {
                    SPACE:1
                },
                "FINAL_STATE":[1]
            },
            "Variable Type": {
                0: {
                    "i": 1,
                    "c": 3, 
                    "b": 6, 
                    "s": 12
                },
                1: {"n": 2},
                2: {"t": 17},
                
                3: {"h": 4},
                4: {"a": 5},
                5: {"r": 17},

                6: {"o": 7},
                7: {"o": 8},
                8: {"l": 9},
                9: {"e": 10},
                10:{"a": 11},
                11:{"n": 12},

                12: {"t": 13},
                13: {"r": 14},
                14: {"i": 15},
                15: {"n": 16},
                16: {"g": 17},
                17: {},
                "FINAL_STATE" : [17]
            },
            "CHAR": {
                0: {
                    "\'": 1
                },
                1: {
                    LETTER: 2,
                    DIGIT: 2,
                    SPACE: 2,

                    '\'': 3
                },
                2: {
                    '\'': 3
                },
                3 : {},

                "FINAL_STATE" : [3]

            },
            "STR": {
                0: {
                    '"': 1
                },
                1: {
                    '"': 3,

                    SPACE: 2,
                    DIGIT: 2,
                    LETTER: 2

                },
                2: {
                    SPACE: 2,
                    DIGIT: 2,
                    LETTER: 2,

                    '"':3
                },
                3: {},

                "FINAL_STATE" : [3]
            },

            "INTEGER": {
                0: {
                    "0": 1,
                    "-": 2,
                    DIGIT_WITHOUT_ZERO:3
                },
                1: {},
                2: {DIGIT_WITHOUT_ZERO: 4},
                3: {DIGIT: 5},
                4: {DIGIT: 5},
                5: {DIGIT: 5},

                "FINAL_STATE": [1, 3, 4, 5]
            },

            "ID": {
                0: {
                    "_": 1,
                    LETTER: 1
                },
                1: {
                    "_": 1,
                    DIGIT: 1,
                    LETTER: 1
                },

                "FINAL_STATE": [1]
            },
            "SEMI": {
                0: {";" :1},
                1: {},

                "FINAL_STATE": [1]

            },
            "LBRACE" : {
                0: {"{" :1},
                1: {},

                "FINAL_STATE": [1]
            },
            "RBRACE" : {
                0: {"}" :1},
                1: {},

                "FINAL_STATE": [1]
            },
            "LPAREN" : {
                0: {"(" :1},
                1: {},

                "FINAL_STATE": [1]
            },
            "RPAREN" : {
                0: {")" :1},
                1: {},

                "FINAL_STATE": [1]
            },
            "LBRACKET" : {
                0: {"[" :1},
                1: {},

                "FINAL_STATE": [1]
            },
            "RBRACKET" : {
                0: {"]" :1},
                1: {},

                "FINAL_STATE": [1]
            },
            "COMMA" : {
                0: {"," :1},
                1: {},

                "FINAL_STATE": [1]
            },
            "OP": {
                0: {
                    # arithmetic operator
                    "+": 1,
                    "-": 1,
                    "*": 1,
                    "/": 1,

                    # assign operator

                    "=": 2,

                    # comparison operator

                    "<": 2,
                    ">": 2,
                    "!": 4

                },

                1: {},
                2: {
                    "=": 3
                },
                3: {},
                4: {
                    "=": 3
                },
                "FINAL_STATE": [1,2,3]
            }, 


            "VTYPE": [
                "int",
                "char",
                'string',
                'boolean',
            ],
            
            "KEYWORD": [
                "if",
                "else",
                "while",
                "class",
                "return",
                "true",
                "false"

            ],

            "UNDEFINED": []
            
        }
 

