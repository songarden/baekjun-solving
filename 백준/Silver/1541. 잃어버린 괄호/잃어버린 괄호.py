from collections import deque
import heapq
import re
import sys


input_string = sys.stdin.readline().strip()

input_operand = re.findall(r'([+-])',input_string)
input_int = re.findall(r'(\d+)',input_string)
input_int = [int(token)if token.isdigit() else token for token in input_int]
result = 0
temp = 0
for i in range(len(input_int)):
    if i == 0:
        result = input_int[i]
    else:
        if input_operand[i-1] == '-':
            if temp == 0:
                temp += input_int[i]
            else:
                result -= temp
                temp = input_int[i]
        else:
            if temp == 0:
                result += input_int[i]
            else:
                temp += input_int[i]

print(result-temp)