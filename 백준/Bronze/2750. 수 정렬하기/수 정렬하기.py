import sys

def quick_sort(numbers,left,right):
    pivot = numbers[(left+right)//2]
    pl = left
    pr = right
    while pl <= pr :
        while numbers[pl] < pivot :
            pl = pl+1
        while numbers[pr] > pivot :
            pr = pr-1
        if pl <= pr :
            numbers[pl],numbers[pr] = numbers[pr],numbers[pl]
            pl = pl+1
            pr = pr-1
    
    if pr > left :
        quick_sort(numbers,left,pr)

    if pl < right :
        quick_sort(numbers,pl,right)



testcase = int(sys.stdin.readline())
numbers = []
for i in range(testcase):
    number = int(sys.stdin.readline())
    numbers.append(number)

quick_sort(numbers,0,len(numbers)-1)

for i in range(testcase):
    print(numbers[i])