import sys

a,b,v = map(int,sys.stdin.readline().split())


if a >= v :
    print(1)
    
else:
    if (v-a) % (a-b) == 0:
        print((v-a)//(a-b) + 1)
    else:
        print((v-a)//(a-b) + 2)

#a-b >= v-a 까지 a-b를 n으로 곱하기