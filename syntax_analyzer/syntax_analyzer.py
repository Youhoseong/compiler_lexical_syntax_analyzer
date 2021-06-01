import sys
import CFG
import slrtable
#infile = sys.argv[1]
#infile = 'codein.java'
#fileinput = open(infile, 'r')
#filewrite = open("codeout.txt", 'w')
#input = fileinput.read()
# print(input)

tempInput = "VTYPE ID SEMI"


fileInput = open("codeout.txt", 'r')
inputList = fileInput.read().split('\n')

tokenList = []
for inputs in inputList:
    token = inputs.split(',')
    tokenList.append(token[0][1:])

print(tokenList)

stack = []
slrTable = slrtable.TableOfSLR().table
actionTable = slrTable["ACTION"]
gotoTable = slrTable["GOTO"]

cfg = CFG.CFG().cfg

stack.append(0)

right = tempInput.split(' ')
left = []
right.append('$')
currentInput = right[0]

while right is not None:  # think!

    while True:
        decision = actionTable[currentInput][stack[-1]]

        if decision[0] == "ACC":
            break

        if decision[0] == "S":
            stack.append(decision[1])
            left.append(currentInput)
            del right[0]
            currentInput = right[0]

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

    print("ACCEPT")
