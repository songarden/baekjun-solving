import sys


def askii(a) :
    return ord(a)


a = sys.stdin.readline().rstrip()
print(askii(a))