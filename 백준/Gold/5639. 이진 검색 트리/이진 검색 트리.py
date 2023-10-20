import sys
sys.setrecursionlimit(10**8)

tree = []

while True:
    try:
#        node = int(sys.stdin.readline().rstrip())
        tree.append(int(sys.stdin.readline().rstrip()))
    except:
        break

def solve(tree,start,end):
    if start>end:
        return
    mid = end+1
    for i in range(start+1,end+1):
        if tree[start] < tree[i]:
            mid = i
            break
    solve(tree,start+1,mid-1)
    solve(tree,mid,end)
    print(tree[start])

solve(tree,0,len(tree)-1)
    
    