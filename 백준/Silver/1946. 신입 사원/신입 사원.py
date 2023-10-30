from collections import deque
import heapq
import re
import sys
sys.setrecursionlimit(10**8)

testCase = int(sys.stdin.readline())
result = [0 for _ in range(testCase)]

for j in range(testCase):
    member_num = int(sys.stdin.readline())
    members = [0 for _ in range(member_num+1)]

    for i in range(member_num):
        a_test , b_test = map(int,sys.stdin.readline().strip().split())
        members[a_test] = b_test

    max_score = member_num+1
    for i in range(1,member_num+1):
        if members[i] < max_score:
            max_score = members[i]
            result[j] += 1

for i in range(testCase):
    print(result[i])