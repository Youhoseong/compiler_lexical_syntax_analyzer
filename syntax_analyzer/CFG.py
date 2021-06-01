
class CFG:
    cfg = {

    }

    tokenConveter = {

    }

    def __init__(self):
        self.cfg = {
            0: {
                "VDECL CODE": "CODE"
            },
            1: {
                "FDECL CODE": "CODE"
            },
            2: {
                "CDECL CODE": "CODE"
            },
            3: {
                '': "CODE",
            },
            4: {
                "VTYPE ID SEMI": "VDECL"
            },
            5: {
                "VTYPE ASSIGN SEMI": "VDECL"
            },
            6: {
                "ID ASSIGN RHS": "ASSIGN"
            },
            7: {
                "EXPR": "RHS"
            },
            8: {
                "LITERAL": "RHS"
            },
            9: {
                "CHARACTER": "RHS"
            },
            10: {
                "BOOLSTR": "RHS"
            },
            11: {
                "T ADDSUB EXPR": "EXPR"
            },

            12: {
                "T": "EXPR"
            },
            13: {
                "F MULDIV T": "T"
            },
            14: {
                "F": "T"
            },
            15: {
                "LPAREN EXPR RPAREN": "F"
            },
            16: {
                "ID": "F"
            },
            17: {
                "NUM": "F"
            },
            18: {
                "VTYPE ID LPAREN ARG RPAREN LBRACE BLOCK RETURN RBRACE": "FDECL"
            },
            19: {
                "VTYPE ID MOREARGS": "ARG"
            },
            20: {
                '': "ARG"
            },
            21: {
                "COMMA VTYPE ID MOREARGS": "MOREARGS"
            },

            22: {
                '': "MOREARGS"
            },
            23: {
                "STMT BLOCK": "BLOCK"
            },
            24: {
                '': "BLOCK"
            },
            25: {
                "VDECL": "STMT"
            },
            26: {
                "ASSIGN SEMI": "STMT"
            },
            27: {
                "IF LPAREN COND RPAREN LBRACE BLOCK RBRACE ELSE": "STMT"
            },

            28: {
                "WHILE LPAREN COND RPAREN LBRACE BLOCK RBRACE": "STMT"
            },

            29: {
                "COND COMP A": "COND"
            },

            30: {
                "BOOLSTR": "COND"
            },
            31: {
                "BOOLSTR": "A"
            },
            32: {
                "ELESE LBRACE BLOCK RBRACE": "ELSE"
            },
            33: {
                '': "ELSE"
            },
            34: {
                "RETURN RHS SEMI": "RETURN"
            },
            35: {
                "CLASS ID LBRACE ODECL RBRACE": "CDECL"
            },
            36: {
                "VDECL ODECL": "ODECL"
            },
            37: {
                "FDECL ODECL": "ODECL"
            },
            38: {
                '': "ODECL"
            }

        }

        self.tokenConveter = {

        }
