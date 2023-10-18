from collections import deque
import copy
import sys
import heapq

words = list(map(str,sys.stdin.readline().strip()))
count = 0

def check_is_right():
    global count
    state = None  #open = "O" #close = "C"
    if len(words) %2 == 1:
        return 0
    stack = [0]
    temp = 1
    while words:
        word = words.pop(0)
        if word == '(' or word == '[':
            if word == '(':
                temp *= 2
            else :
                temp *= 3
            stack.append(word)
            state = "O"
        elif word == ')' or word == ']':
            check = stack.pop()
            if check == '(' and word == ')':
                if state == "O":
                    count += temp
                temp //= 2
                state = "C"
            elif check == '[' and word == ']':
                if state == "O":
                    count += temp
                temp //=3
                state = "C"
            else :
                return 0
    return count

print(check_is_right())