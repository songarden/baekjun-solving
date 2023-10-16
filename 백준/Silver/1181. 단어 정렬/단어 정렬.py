import sys

n = int(sys.stdin.readline())
textList = []
for i in range(n):
    text = sys.stdin.readline().strip()
    textList.append(text)
textList = sorted(set(textList))
textList = sorted(textList , key= lambda x:(len(x),x) )

for i in textList :
    print(i)
