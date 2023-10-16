import sys
import heapq

import sys

testCase = int(sys.stdin.readline())
numbers = []
for i in range(testCase):
    num = int(sys.stdin.readline())
    numbers.append(num)

numbers = sorted(numbers)

for i in numbers :
    print(i)