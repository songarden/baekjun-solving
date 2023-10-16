import sys

babies = []

for i in range(9):
    height = int(sys.stdin.readline())
    babies.append(height)

# for i in range(7):
#     real_babies.append(babies[i])

def sum_babies(babies):
    sum = 0
    for i in babies:
        sum += i
    return sum

for i in range(0,8):
    for j in range(i+1,9):
        fake = babies[i]+babies[j]
        real_sum = sum_babies(babies)-fake
        if real_sum == 100:
            if i>j :
                babies.pop(i)
                babies.pop(j)
            else:
                babies.pop(j)
                babies.pop(i)
            break;
    if len(babies) == 7:
        break;

babies = sorted(babies)
for i in babies:
    print(i)