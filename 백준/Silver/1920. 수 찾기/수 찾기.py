from collections import deque
import sys
n = int(sys.stdin.readline())
first_line = list(map(int ,sys.stdin.readline().split()))
first_line = sorted(first_line)
m = int(sys.stdin.readline())
sec_line = list(map(int,sys.stdin.readline().split()))
result = []

def search_binary(a): #a라는 데이터가 있는지 검색하는 이진 탐색 함수
    global n
    pl = 0
    pr = n-1
    while True :
        pc = (pl+pr)//2
        if a == first_line[pc]:
            return 1
        elif a < first_line[pc]:
            pr = pc-1
        else:
            pl = pc +1
        if pl>pr:
            return 0

for i in sec_line:
    answer = search_binary(i)
    print(answer)