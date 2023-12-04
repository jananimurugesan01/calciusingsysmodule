import sys
operation= sys.argv[0]
a=int(sys.argv[1])
b=int(sys.argv[2])
if operation=="add":
    print(a+b)
elif operation=="sub":
    print(a-b)
elif operation=="mul":
    print(a*b)
elif operation=="div":
    print(a/b)
