import sys


testcase = int(sys.stdin.readline())
repeat_num = []
word_result = []
for i in range(testcase):
    repeat, word = sys.stdin.readline().split()
    repeat = int(repeat) ## 3
    repeat_num.append(repeat)
    temp = list(word) ## ['a','b','c']
    word_result.append('')
    for a in temp :
        a = a*repeat
        word_result[i] = word_result[i]+a
        
    # print(''.join(map(str,word_result[i])))


for i in range(testcase):
    print(''.join(map(str,word_result[i])))