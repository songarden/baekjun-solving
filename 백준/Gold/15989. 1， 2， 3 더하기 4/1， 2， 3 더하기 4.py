import sys

testcase = int(sys.stdin.readline())

for _ in range(testcase):
    n = int(sys.stdin.readline())
    result = 1
    result += n//2
    result += n//3
    
    while(n >= 5):
        result += (n-5)//2 + 1
        n -= 3
    
    print(result)