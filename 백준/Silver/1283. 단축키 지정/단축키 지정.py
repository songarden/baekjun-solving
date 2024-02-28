import sys

n = int(sys.stdin.readline())

dict = {}
result = []

for i in range(n) :
    thisAlpha = sys.stdin.readline().strip()
    words = thisAlpha.split()
    temp = ''
    for wNum in range(len(words)) :
        if not words[wNum][0] in dict :
            dict[words[wNum][0]] = True
            if words[wNum][0].upper() == words[wNum][0] :
                dict[words[wNum][0].lower()] = True
            else :
                dict[words[wNum][0].upper()] = True
            words[wNum] = '['+words[wNum][0]+']'+words[wNum][1:]
            result.append(" ".join(words))
            break
    if len(result) == i :
        for wordN in range(len(thisAlpha)) :
            if not thisAlpha[wordN] == ' ' and not thisAlpha[wordN] in dict :
                # result.append(thisAlpha.replace(word, '['+word+']'))
                dict[thisAlpha[wordN]] = True
                if thisAlpha[wordN].upper() == thisAlpha[wordN] :
                    dict[thisAlpha[wordN].lower()] = True
                else :
                    dict[thisAlpha[wordN].upper()] = True
                result.append(thisAlpha[:wordN] + '[' + thisAlpha[wordN] + ']' + thisAlpha[wordN+1:])
                break
    if len(result) == i :
        result.append(thisAlpha)

for ans in result :
    print(ans)