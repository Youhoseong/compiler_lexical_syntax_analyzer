
class CFG:
    cfg = {

    }

    tokenConverter = {

    }

    def __init__(self):
        self.cfg = {
            0: {
                "CODE": "START"
            },
            1: {
                "VDECL CODE": "CODE"
            },
            2: {
                "FDECL CODE": "CODE"
            },
            3: {
                "CDECL CODE": "CODE"
            },
            4: {
                '': "CODE",
            },
            5: {
                "VTYPE ID SEMI": "VDECL"
            },
            6: {
                "VTYPE ASSIGN SEMI": "VDECL"
            },
            7: {
                "ID assign RHS": "ASSIGN"
            },
            8: {
                "EXPR": "RHS"
            },
            9: {
                "LITERAL": "RHS"
            },
            10: {
                "CHARACTER": "RHS"
            },
            11: {
                "BOOLSTR": "RHS"
            },
            12: {
                "T ADDSUB EXPR": "EXPR"
            },

            13: {
                "T": "EXPR"
            },
            14: {
                "F MULDIV T": "T"
            },
            15: {
                "F": "T"
            },
            16: {
                "LPAREN EXPR RPAREN": "F"
            },
            17: {
                "ID": "F"
            },
            18: {
                "NUM": "F"
            },
            19: {
                "VTYPE ID LPAREN ARG RPAREN LBRACE BLOCK RETURN RBRACE": "FDECL"
            },
            20: {
                "VTYPE ID MOREARGS": "ARG"
            },
            21: {
                '': "ARG"
            },
            22: {
                "COMMA VTYPE ID MOREARGS": "MOREARGS"
            },

            23: {
                '': "MOREARGS"
            },
            24: {
                "STMT BLOCK": "BLOCK"
            },
            25: {
                '': "BLOCK"
            },
            26: {
                "VDECL": "STMT"
            },
            27: {
                "ASSIGN SEMI": "STMT"
            },
            28: {
                "IF LPAREN COND RPAREN LBRACE BLOCK RBRACE ELSE": "STMT"
            },

            29: {
                "WHILE LPAREN COND RPAREN LBRACE BLOCK RBRACE": "STMT"
            },

            30: {
                "COND COMP A": "COND"
            },

            31: {
                "BOOLSTR": "COND"
            },
            32: {
                "BOOLSTR": "A"
            },
            33: {
                "else LBRACE BLOCK RBRACE": "ELSE"
            },
            34: {
                '': "ELSE"
            },
            35: {
                "return RHS SEMI": "RETURN"
            },
            36: {
                "CLASS ID LBRACE ODECL RBRACE": "CDECL"
            },
            37: {
                "VDECL ODECL": "ODECL"
            },
            38: {
                "FDECL ODECL": "ODECL"
            },
            39: {
                '': "ODECL"
            }

        }

        self.tokenConverter = {
            "FALSE": "BOOLSTR",
            "TRUE": "BOOLSTR",
            "STR": "LITERAL",
            "INTEGER": "NUM",
            "CHAR": "CHARACTER",

            "+": "ADDSUB",
            "-": "ADDSUB",

            "*": "MULDIV",
            "/": "MULDIV",

            "<": "COMP",
            ">":  "COMP",
            "==": "COMP",
            ">=": "COMP",
            "<=": "COMP",
            "!=": "COMP",

            "=": "assign",
            "ELSE": "else",
            "RETURN": "return"
        }
