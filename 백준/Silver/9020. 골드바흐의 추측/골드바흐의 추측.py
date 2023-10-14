import sys
import math

def isPrime(x):
    if(i == 1):
        return False
    point_num = int(math.sqrt(x))
    for j in range(2,point_num+1):
        if(x%j == 0):
            return False
    return True


testCase = int(sys.stdin.readline())
numbers = []
for i in range(testCase):
    a = int(sys.stdin.readline())
    numbers.append(a)
## numbers = [8,10,16]
result = []
for i in numbers :
    point_num = 0
    if (i/2)%2 == 0 and i>4:
        point_num = int((i/2)+1)
    else :
        point_num = int(i/2)
    while(1):
        if isPrime(point_num) and isPrime(i-point_num):
            break;
        point_num+=2
    result.append([i-point_num,point_num])

for x in result:
    print(' '.join(map(str,x)))