import sys
import CFG
import slrtable
# terminal 상에서 codeout파일을 매개변수로 받기 위한 설정
infile = sys.argv[1]

# codeout.txt read를 위한 코드
fileInput = open(infile, 'r')
inputList = fileInput.read().split('\n')


tokenConverter = CFG.CFG().tokenConverter
cfg = CFG.CFG().cfg
slrTable = slrtable.TableOfSLR().table
actionTable = slrTable["ACTION"]
gotoTable = slrTable["GOTO"]

tokenList = []
tokenValueList = []
lineInfoList = []

# lexical 결과를 통해 얻은 token set 정보에서 token name, value, line information 등의 내용 각각을 list로 가져옴
for inputs in inputList:  # <OP, =>
    token = inputs.split(',')

    if token[0][1:] == '':
        continue

    # token name이 operator일때 더 구체적인 token name부여를 위한 작업
    if token[0][1:] == "OP":
        tokenList.append(tokenConverter[token[1][1:]])
    elif token[0][1:] in list(tokenConverter.keys()):
        tokenList.append(tokenConverter[token[0][1:]])
    else:
        tokenList.append(token[0][1:])

    tokenValueList.append(token[1][1:])
    lineInfoList.append(token[2][1:-1])

# 두 개의 subgroup list 생성
right = tokenList
left = []

# right에 '$' 추가
right.append('$')
currentInput = right[0]
currentInputCount = 0
stack = []

# 스택에 state 0 정보 초기화
stack.append(0)

# 에러 유무 판단 변수
isError = False

# syntax analyze 시작
while True:
    # stack의 top과 currentInput으로 action table 조회
    if stack[-1] not in list(actionTable[currentInput].keys()):
        # action table 값이 없을 때 에러 발생 후 syntax analyze 종료
        isError = True
        break

    else:
        # 값이 있을 때 다음 동작 받아옴
        decision = actionTable[currentInput][stack[-1]]

    # 다음 동작이 ACCEPT 라면 syntax analyze 완료. => 종료
    if decision[0] == "ACC":
        break

    # shift 동작 수행
    if decision[0] == "S":
        stack.append(decision[1])
        left.append(currentInput)
        del right[0]
        currentInput = right[0]
        currentInputCount += 1

    # reduce 동작 수행
    elif decision[0] == "R":
        cfgNum = decision[1]
        curCFG = cfg[cfgNum]
        cfgKey = list(curCFG.keys())[0]

        if cfgKey == '':
            count = 0
        else:
            count = cfgKey.count(' ')+1

        if count > 0:
            del left[-count:]
            del stack[-count:]

        left.append(curCFG[cfgKey])

        # goto table 조회
        gotoDecision = gotoTable[left[-1]][stack[-1]]
        stack.append(gotoDecision)


print("#######################################")
print()

# 에러 발생 여부 체크
if isError == False:
    # 에러 없을 시 ACCEPT
    print("# ACCEPT, There is No Error.")
else:
    # 에러 있을 시 처리
    print("# REJECT, There is Error.")
    if currentInput == "$":
        lineInfoList.append(int(lineInfoList[currentInputCount-1])+1)

    # 각 문장의 마지막 요소에 에러가 있을 때의 처리
    if lineInfoList[currentInputCount-1] != lineInfoList[currentInputCount]:
        currentInputCount -= 1

        # 오류 발생 line 정보 출력
        print("# Reject from Line Number:",
              lineInfoList[currentInputCount-1])
        print("# Last token of ", end='')
        print("[   ", end='')
        for i in range(len(lineInfoList)):
            if lineInfoList[i] == lineInfoList[currentInputCount]:
                print(tokenValueList[i], end=' ')
        print("  ] is missing.")

    # 각 문장의 중간 요소에 에러가 있을 때의 처리
    else:
        # 오류 발생 line 정보 출력
        print("# Reject from Line Number:",
              lineInfoList[currentInputCount])
        print("# [   ", tokenValueList[currentInputCount], "   ] of ", end='')
        print("[   ", end='')
        for i in range(len(lineInfoList)):
            if lineInfoList[i] == lineInfoList[currentInputCount]:
                print(tokenValueList[i], end=' ')

        print("  ] is not expected.")
print()
print("#######################################")
