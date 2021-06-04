import sys
import CFG
import slrtable
#infile = sys.argv[1]
#infile = 'codein.java'
#fileinput = open(infile, 'r')
#filewrite = open("codeout.txt", 'w')
#input = fileinput.read()
# print(input)

fileInput = open("codeout.txt", 'r')
inputList = fileInput.read().split('\n')

tokenConverter = CFG.CFG().tokenConverter
cfg = CFG.CFG().cfg
slrTable = slrtable.TableOfSLR().table
actionTable = slrTable["ACTION"]
gotoTable = slrTable["GOTO"]

tokenList = []
tokenValueList = []
lineInfoList = []
for inputs in inputList:  # <OP, =>
    token = inputs.split(',')
    print(token)
    if token[0][1:] == '':
        continue

    if token[0][1:] == "OP":
        print(token[1][1:])
        tokenList.append(tokenConverter[token[1][1:]])
    elif token[0][1:] in list(tokenConverter.keys()):
        tokenList.append(tokenConverter[token[0][1:]])
    else:
        tokenList.append(token[0][1:])

    tokenValueList.append(token[1][1:])
    lineInfoList.append(token[2][1:-1])

print(tokenList)
print(tokenValueList)
print(lineInfoList)


right = tokenList
left = []
right.append('$')
currentInput = right[0]
currentInputCount = 0
stack = []
stack.append(0)


isError = False

while True:
    print("현재input:", currentInput)
    print("currentInputCount:", currentInputCount)
    print("right:", right)
    print("left: ", left)
    print("stack:", stack)
    print()

    if stack[-1] not in list(actionTable[currentInput].keys()):
        isError = True
        break
    else:
        decision = actionTable[currentInput][stack[-1]]

    print(decision)
    print()

    if decision[0] == "ACC":
        break

    if decision[0] == "S":
        stack.append(decision[1])
        left.append(currentInput)
        del right[0]
        currentInput = right[0]
        currentInputCount += 1

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
        gotoDecision = gotoTable[left[-1]][stack[-1]]
        stack.append(gotoDecision)


print("#######################################")
print()
# if ( false
# {

# }


if isError == False:
    print("# ACCEPT, There is No Error.")
else:
    print("# REJECT, There is Error.")
    if currentInput == "$":
        lineInfoList.append(int(lineInfoList[currentInputCount-1])+1)

    if lineInfoList[currentInputCount-1] != lineInfoList[currentInputCount]:
        currentInputCount -= 1
        print("# Reject from Line Number:",
              lineInfoList[currentInputCount-1])
        print("# Last token of ", end='')
        print("[   ", end='')
        for i in range(len(lineInfoList)):
            if lineInfoList[i] == lineInfoList[currentInputCount]:
                print(tokenValueList[i], end=' ')
        print("  ] is missing.")

    else:
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
