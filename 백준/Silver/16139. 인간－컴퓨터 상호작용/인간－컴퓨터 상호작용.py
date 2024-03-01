import sys

word = sys.stdin.readline()

dict = {}

for i in range(len(word)) :
    if not word[i] in dict:
        dict[word[i]] = [i]
    else :
        dict[word[i]].append(i)

test = int(sys.stdin.readline())
result = [0 for _ in range(test)]

for i in range(test):
    alpha,s,e = map(str,sys.stdin.readline().split())
    start = int(s)
    end = int(e)
    if not alpha in dict:
        continue
    else:
        for indexes in dict[alpha] :
            if indexes < start :
                continue
            if indexes > end:
                break
            result[i] += 1

for ans in result :
    print(ans)
            