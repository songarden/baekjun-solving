import sys
sys.setrecursionlimit(2500)
s = sys.stdin.readline().rstrip()
t = sys.stdin.readline().rstrip()
cani = 0

def search(x):
    global cani
    if (s == x):
        cani = 1
        return
    if len(x) == 1 or cani == 1:
        return
    if x[-1] == 'A' :
        search(x[:-1])
    elif x[-1] == 'B' :
        temp = x[:-1]
        search(temp[::-1])

search(t)
print(cani)