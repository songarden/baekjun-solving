from collections import deque
import heapq
import re
import sys
sys.setrecursionlimit(10**8)

fst_word = sys.stdin.readline().strip()
fst_len = len(fst_word)
sec_word = sys.stdin.readline().strip()
sec_len = len(sec_word)
lcs_list = [[0 for _ in range(fst_len+1)] for _ in range(sec_len+1)]
# 인덱스 0 은 0으로 초기화
count = 0
if fst_len and sec_len:
    for i in range(1,sec_len+1):
        #CAPCAK
        for j in range(1,fst_len+1):
            #ACAYKP
            if fst_word[j-1] == sec_word[i-1]:
                lcs_list[i][j] = lcs_list[i-1][j-1] + 1
            else:
                lcs_list[i][j] = max(lcs_list[i-1][j],lcs_list[i][j-1])

print(lcs_list[sec_len][fst_len])