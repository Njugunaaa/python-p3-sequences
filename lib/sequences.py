#!/usr/bin/env python3

def print_fibonacci(length):
    fibonacci=[]
    if length<=0:
        print(fibonacci)
        return
    elif length ==1:
        print([0])
        return
    elif length ==2:
        print([0,1])
        return
    fibonacci=[0,1]

    while len(fibonacci)<length:
        next_value=fibonacci[-1] + fibonacci[-2]
        fibonacci.append(next_value)

    print(fibonacci)
