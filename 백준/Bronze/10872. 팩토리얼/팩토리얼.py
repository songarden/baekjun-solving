import sys

def factorial(x) :
    if x<= 1 :
        return 1
    else :
        return x*factorial(x-1)

x = int(sys.stdin.readline())
print(factorial(x))