from collections import deque
import sys
import heapq

m, n, l = map(int,sys.stdin.readline().strip().split())
gun = list(map(int,sys.stdin.readline().split()))
gun = sorted(gun)
catch = 0
animals = []
for i in range(n):
    animal = list(map(int,sys.stdin.readline().split()))
    if animal[1] <= l:
        animals.append(animal)

def search_binary(animal_x):
    global m
    pl = 0
    pr = m-1
    while True:
        pc = (pl+pr)//2
        if gun[pc] == animal_x:
            return pc
        elif gun[pc] > animal_x:
            pr = pc-1
        else :
            pl = pc+1
        if pr < 0 :
            return 0
        if pl > m-1:
            return m-1
        if pl>pr:
            if abs(gun[pl]-animal_x) > abs(gun[pr]-animal_x):
                return pr
            else :
                return pl

for i in animals:
    nearest_gun_index = search_binary(i[0])
    if abs(i[0]-gun[nearest_gun_index])+i[1] <= l:
        catch +=1
print(catch)