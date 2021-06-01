import sys
import CFG
import slrtable
#infile = sys.argv[1]
#infile = 'codein.java'
#fileinput = open(infile, 'r')
#filewrite = open("codeout.txt", 'w')
#input = fileinput.read()
#print(input)

tempInput = "VTYPE ID SEMI"

stack = []
slrTable = slrtable.TableOfSLR().table
actionTable = slrTable["ACTION"]
gotoTable = slrTable["GOTO"]

cfg = CFG.CFG().cfg

stack.append(0)

right = tempInput.split(' ')
left = []
right.append('$')
print(right)
currentInput = right[0]
while True:
    print("left", left)
    print("right", right)
    print("Stack",stack)
    print("curInput",currentInput)
    decision = actionTable[currentInput][stack[-1]]
    print(decision)

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
        #print(curCFG)
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