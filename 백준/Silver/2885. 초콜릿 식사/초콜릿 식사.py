import sys
import math

n = int(sys.stdin.readline())
choco = n if int(math.log2(n)) == math.log2(n) else 2**(int(math.log2(n))+1)
leftPeices = choco - n 
cut = 0
while (leftPeices != 0 ):
    
    if choco/(2**cut) <= leftPeices:
        leftPeices -= choco/(2**cut)
    else :
        cut += 1

print(choco,cut)