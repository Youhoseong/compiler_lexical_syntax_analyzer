from dfatable import TableofDFA
import string


def giveTokenToSingleInput(i):
    if i.isalpha():
        return "ID"
    elif i == '_':
        return "ID"
    elif i.isdigit():
        return "INTEGER"
    elif i in ['+', '-', '*', '/', '!', '<', '>', '=']:
        return "OP"
    elif i in ['{']:
        return "LBRACE"
    elif i in ['}']:
        return "RBRACE"
    elif i in ['(']:
        return "LPAREN"
    elif i in [')']:
        return "RPAREN"
    elif i in ['[']:
        return "LBRACKET"
    elif i in [']']:
        return "RBRACKET"
    elif i in [';']:
        return "SEMI"
    elif i in [',']:
        return "COMMA"
    elif i in ['"']:
        return "STR"
    elif i in ["'"]:
        return "CHAR"
    elif i in string.whitespace:
        return "WHITE_SPACE"
    else:
        return "UNDEFINED"

def start_analyze(input, cs):
   
    global currentState
    global fileWrite
    global lexical_token_list
    global currentToken

    currentState = cs
    # 1은 토큰 분류 중, 0은 입력값과 토큰 불일치
    token_dic = table[currentToken] 

    if currentToken in ["ID", "INTEGER", "CHAR", "STR"]:
        flag = 0
        keyList = list(token_dic[currentState].keys())
   
        for keylist in keyList:
            if input in keylist:
                flag=1
                if currentToken in ["CHAR", "STR"]:
                    if input not in ["'", "\""]:
                        lexeme.append(input)
                else:
                    lexeme.append(input)
                currentState = token_dic[currentState][keylist]
            
        if flag == 0 and currentState in token_dic["FINAL_STATE"]:
            str = ""
            if currentToken == "ID":
                keyword_list = table["VTYPE"] + table["KEYWORD"]
                if ''.join(lexeme) in keyword_list[:4]:
                    str = ["VTYPE", ''.join(lexeme)]
                elif ''.join(lexeme) in keyword_list[4:]:
                    str = [''.join(lexeme).upper(), ''.join(lexeme)]
                else:
                    str = [currentToken, ''.join(lexeme)]
            else:
                str = [currentToken, ''.join(lexeme)]

            lexical_token_list.append(str)
            lexeme.clear()
 
            return 0
 
    elif currentToken in ["UNDEFINED"]:
        lexical_token_list.append([currentToken, ''.join(lexeme)])
        return 0
    elif currentToken in ["WHITE_SPACE"]:
        return 0
    else:
        if input in token_dic[currentState]:
            lexeme.append(input)
            currentState = token_dic[currentState][input]
            return 1
        else:
            if currentState in token_dic["FINAL_STATE"]:
       
                lexical_token_list.append([currentToken, ''.join(lexeme)])
                lexeme.clear()
   
            return 0

def isMinusOperator(result):
    delList= []
    for index in range(0, len(result)-1):

        if index==0 and result[index][1] == '-' and result[index+1][0] in ['INTEGER'] and result[index+1][1] != '0':
            result[index+1][1] = '-' + result[index+1][1]
            delList.append(index)
        elif result[index][1] == '-':
            if result[index-1][0] not in ['RPAREN', 'INTEGER', 'ID'] and result[index+1][0] in ['INTEGER'] and result[index+1][1] != '0':
                result[index+1][1] = '-' + result[index+1][1]
                delList.append(index)

    delList.reverse()

    for deleteindex in delList:
        del result[deleteindex]

    return result 

tableClass = TableofDFA()
table = tableClass.table
lexeme=[]
lexical_token_list = []

fileInput = open('codein.txt', 'r')
fileWrite = open("codeout.txt", 'w')
input = fileInput.read() + " "

currentToken = giveTokenToSingleInput(input[0])
currentState = 0
status = 1

for i in range(0,len(input)):

    if status != 0:
        status = start_analyze(input[i], currentState)

    if status == 0:
        currentToken = giveTokenToSingleInput(input[i]) # 토큰 업데이트
        currentState = 0 
        status = start_analyze(input[i], currentState)
        status = 1 # 토큰 업데이트 안해도 되는 상황 

for i in lexical_token_list:
    fileWrite.write(str(i))
    fileWrite.write('\n')

fileWrite.write('------------------------\n')

lexical_token_list = isMinusOperator(lexical_token_list)

for i in lexical_token_list:
    printStr = f"<{i[0]}, {i[1]}>"
    fileWrite.write(printStr)
    fileWrite.write('\n')

    



    
    


    
