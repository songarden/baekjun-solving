import sys

testCase = int(sys.stdin.readline())
result = []

for i in range(testCase):
    n = int(sys.stdin.readline())
    tongTree = list(map(int,sys.stdin.readline().split()))
    tongTree.sort()
    # print(tongTree)
    tongTreeLeft = []
    for j in range(0,n-1, 2):
        tongTreeLeft.append(tongTree[j])
    tongTreeLeft.append(tongTree[-1])
    nextI = n-2
    if n%2 == 0:
        nextI = n-3
    for j in range(nextI,0, -2):
        tongTreeLeft.append(tongTree[j])
    # print(tongTreeLeft)
    hard = 0
    for k in range(n):
        hard = max(hard, abs(tongTreeLeft[k]-tongTreeLeft[k-1]))
    result.append(hard)

for ans in result:
    print(ans)