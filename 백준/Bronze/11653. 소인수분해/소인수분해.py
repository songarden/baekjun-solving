import sys
import math

n = int(sys.stdin.readline())
if n == 1:
    sys.exit()
i = 2
result = []
isDecimal = True
while n != 1:
    if i > 3 and not isDecimal:
        if i % 2 == 0 or i % 3 == 0:
            i = i+1
            continue
        k = int(math.sqrt(i))
        for j in range(2,k):
            if i % j == 0:
                isDecimal = False
                break
            else:
                isDecimal = True
        if not isDecimal :
            i = i+1
            continue
    if n % i == 0:
        result.append(i)
        n = n//i
    else:
        i = i+1
        isDecimal = True

# sorted(result)

for i in result:
    print(i)