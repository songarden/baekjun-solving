import sys
import math

##소수인지 확인하려면 해당 수의 제곱근을 반올림한 자연수까지
##나눴을때 나눠 떨어지는지 확인한다.

testCase = int(sys.stdin.readline())
numbers = list(map(int,sys.stdin.readline().split()))
result = 0
for i in numbers:
    if(i == 1):
        continue
    result+=1
    point_num = int(math.sqrt(i))
    for j in range(2,point_num+1):
        if(i%j == 0):
            result -= 1
            break

print(result)