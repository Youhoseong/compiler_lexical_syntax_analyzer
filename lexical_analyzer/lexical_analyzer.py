import sys
from dfatable import TableofDFA
import string


lineCount = 1
# 인풋에 대해서 가능한 토큰(후보 토큰)을 부여하는 함수 정의


def giveTokenToSingleInput(i):
    # i가 알파벳 혹은 _라면 ID 토큰 부여
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


# lexcial 분석 함수 정의
def start_analyze(input, cs, lineCount):
    # 이 함수의 반환 값은 토큰 변경 여부이다.
    # 0을 반환하면 input에 대해 부여한 후보 토큰을 변경해야 한다는 의미, 1을 반환하면 이전 input에 대해 부여 받았던 토큰을
    # 유지하면서 analyze하게 된다.

   # 전역변수 사용 선언 부
    global currentState
    global fileWrite
    global lexical_token_list
    global currentToken

    currentState = cs

    # 현재 토큰의 transition table을 가져옴
    token_dic = table[currentToken]

    # 현재 토큰이 ID, INT, CHAR, STR에 해당할 경우
    if currentToken in ["ID", "INTEGER", "CHAR", "STR"]:
        # 인풋이 transition table 상에서 받아들여지는지 여부를 체크하는 변수.
        flag = 0
        keyList = list(token_dic[currentState].keys())

        for keylist in keyList:
            # 인풋이 현재 토큰의 transition table 상에서 정의 돼있는지 확인
            if input in keylist:
                # 정의 돼있으면 flag 변수값 true로 변경
                flag = 1
                # 정의 돼있는 input을 lexeme 리스트에 추가한다.
                lexeme.append(input)

                # transition table에서 input이 들어오면서 변경되는 다음 상태를 업데이트 한다.
                currentState = token_dic[currentState][keylist]

         # 인풋이 transition table 상에 정의 돼있지 않을 때
        if flag == 0:

            # 현재 상태가 final state 라면 지금 까지 분류 했던 lexeme 리스트를 하나의 토큰으로 분류하는 과정임.

            if currentState in token_dic["FINAL_STATE"]:
                str = ""
                # 현재 분류 중인 토큰이 ID(변수)라면,
                if currentToken == "ID":
                    # lexeme 리스트가 키워드에 속하는지 체크한다.
                    keyword_list = table["VTYPE"] + table["KEYWORD"]
                    if ''.join(lexeme) in keyword_list[:4]:
                        # 변수 타입인지 체크
                        str = ["VTYPE", ''.join(lexeme), lineCount]
                    elif ''.join(lexeme) in keyword_list[4:]:
                        str = [''.join(lexeme).upper(),
                               ''.join(lexeme), lineCount]

                    # 키워드에 속하지 않으면 ID로 분류
                    else:
                        str = [currentToken, ''.join(lexeme), lineCount]
                 # 현재 분류 중인 토큰이 CHAR 혹은 STRING이면 앞 뒤 따옴표를 제거하고 토큰 분류한다.
                elif currentToken in ["CHAR", "STR"]:
                    temp_lexeme = ''.join(lexeme)
                    str = [currentToken, temp_lexeme[1:-1], lineCount]
                else:
                    str = [currentToken, ''.join(lexeme), lineCount]
            # 현재 (상태,인풋) 쌍이 transition table에 정의돼있지 않으면서 현재 상태가 final state가 아닐 때
            else:
                # undefined 토큰을 부여한다.
                str = ["Undefined", ''.join(lexeme), lineCount]

            lexical_token_list.append(str)
            lexeme.clear()

            return 0
    # 현재 토큰이 정의돼있지 않을 때
    elif currentToken in ["UNDEFINED"]:
        checkinput = string.digits + string.whitespace + string.ascii_letters
        if input not in checkinput and len(lexeme) < 1:
            lexeme.append(input)
            return 1

        else:
            lexical_token_list.append(
                [currentToken, ''.join(lexeme), lineCount])
            lexeme.clear()

            return 0

   # 현재 토큰이 white space일 때
    elif currentToken in ["WHITE_SPACE"]:

        # 토큰 리스트에 추가하지 않고 함수 종료함
        return 0

    # 나머지 토큰에 대해 분석
    else:
        # (상태,인풋)이 transition table에 정의돼있을 때
        if input in token_dic[currentState]:
            # lexeme 분류 리스트에 추가
            lexeme.append(input)
            currentState = token_dic[currentState][input]

            # 후보 토큰을 바꾸지 않고 유지한다는 의미 => 1 리턴
            return 1
        # transition table에 정의돼있지 않을 때
        else:
            # 현재 상태가 final state면
            if currentState in token_dic["FINAL_STATE"]:
                # 지금까지 분류한 lexeme list에 토큰을 부여한다.
                lexical_token_list.append(
                    [currentToken, ''.join(lexeme), lineCount])
                lexeme.clear()
            # 정의돼있지 않은데 final state도 아니라면
            else:
                # undefined 토큰 부여
                lexical_token_list.append(
                    ["undefined2", ''.join(lexeme), lineCount])

            # 토큰 분류를 완료했으니 새로운 후보 토큰을 부여하라는 의미 => 0 리턴
            return 0

# 토큰 분류를 완료한 토큰 분류 리스트에 대해 -가 operator 토큰인지, integer 토큰로 속하는지 검사하는 함수 정의


def isMinusOperator(result):
    delList = []
    for index in range(0, len(result)-1):
        # operator, -로 분류된 토큰 앞이 닫는 괄호(RPAREN), 정수(INTEGER), 변수(ID)에 속하지 않고, 뒤 토큰이 정수(INTEGER)일 때만 현재 operator, - 토큰을 정수 토큰으로 합침
        if index == 0 and result[index][1] == '-' and result[index+1][0] in ['INTEGER'] and result[index+1][1] != '0':
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


# transition table 불러옴
tableClass = TableofDFA()
table = tableClass.table
lexeme = []
lexical_token_list = []


# file stream 정의
inFile = sys.argv[1]
#inFile = 'codein.java'
fileInput = open(inFile, 'r')
fileWrite = open("codeout.txt", 'w')
input = fileInput.read() + '\n'


# file input의 첫글자에 대해서 후보 토큰을 얻는다.
currentToken = giveTokenToSingleInput(input[0])
currentState = 0
status = 1

# file input에 대해 한글자씩 analyze 시작
for i in range(0, len(input)):

    # status가 0이면, 현재 인풋에 대해 새로운 후보 토큰을 얻고, 그렇지 않을 때는 이전에 얻었던 후보 토큰을 유지하면서 분석 진행

    if status != 0:
        # 현재 인풋에 대해 analyze 진행
        status = start_analyze(input[i], currentState, lineCount)

    # 현재 인풋에 대해 가능한 후보 토큰 얻음
    if status == 0:
        currentToken = giveTokenToSingleInput(input[i])  # 토큰 업데이트
        currentState = 0

        # if currentToken is not "UNDEFINED":
        status = start_analyze(input[i], currentState, lineCount)

        status = 1  # 토큰 업데이트 하고 나서는 업데이트 안하도록 변수 설정

    if input[i] == '\n':
        lineCount += 1

# 토큰 분류 리스트에 대해 -가 operator인지 integer인지 체크함
lexical_token_list = isMinusOperator(lexical_token_list)


# 토큰 분류 파일 출력
for i in lexical_token_list:
    print(i)
    printStr = f"<{i[0]}, {i[1]}, {i[2]}>"
    fileWrite.write(printStr)
    fileWrite.write('\n')


print(lineCount)
print("lexical analyze complete...")
