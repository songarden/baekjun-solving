import sys

n , s , m = map(int,sys.stdin.readline().split())

vol = list(map(int,sys.stdin.readline().split()))

mem = {}

def dp(i, crt) :
    global m
    global n
    max_result = -1
    
    if i in mem :
        if crt in mem[i]:
            return -1
        else:
            mem[i].append(crt)
    else :
        mem[i] = [crt]
        
    if i == n :
        return crt
    
    if crt + vol[i] > m and crt - vol[i] < 0 :
        return -1
    
    if crt + vol[i] <= m :
        max_result = max(dp(i+1,crt+vol[i]) , max_result)
    
    if crt - vol[i] >= 0 :
        max_result = max(dp(i+1,crt-vol[i]) , max_result)
    
    return max_result

print(dp(0,s))