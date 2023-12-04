import sys
operation= sys.argv[0]
operand1=int(sys.argv[1])
operand2=int(sys.argv[2])
if operation=="add":
    print(operand1+operand2)
elif operation=="sub":
    print(operand1-operand2)
elif operation=="mul":
    print(operand1*operand2)
elif operation=="div":
    print(operand1/operand2)
