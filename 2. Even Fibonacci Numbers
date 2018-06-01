
#challenge number 2: Even Fibonnachi Numbers

Total = 0
varOld = 1
varNew = 2
buffer = 0

def checkEven(Total, arg1):
    number = arg1 % 2
    if number == 0:
        return arg1
    else:
        return 0

while varNew < 4000000:

    Total += checkEven(Total, varNew)
    buffer = varNew + varOld
    varOld = varNew
    varNew = buffer
    buffer = 0
    print(varNew)

print("The Total is " + str(Total))
