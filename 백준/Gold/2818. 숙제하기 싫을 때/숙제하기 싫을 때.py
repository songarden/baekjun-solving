import sys

x,y = map(int,sys.stdin.readline().split())
top = 1
front = 2
right = 3

sum = 0

pos_x = 1
pos_y = 1

moving = 3
#left = 1, down = 2, right = 3


def pos (move) :
    global top,front,right
    tmp_t = top
    tmp_f = front
    tmp_r = right
    if move == 1:
        top = tmp_r
        front = tmp_f
        right = 7-tmp_t
    elif move == 2:
        top = 7-tmp_f
        front = tmp_t
        right = tmp_r
    elif move == 3:
        top = 7-tmp_r
        front = tmp_f
        right = tmp_t

div_y = y//4
y = y%4
sum += div_y*14*x

end_x = x
end_y = y if x%2 == 1 else 1

if not y == 0:
    while (1):
        sum += top
        for _ in range(y-1):
            pos(moving)
            sum += top
            if moving == 3:
                pos_y += 1
            else:
                pos_y -= 1
        if pos_x == end_x and pos_y == end_y:
            break
        if not end_x == pos_x:
            pos(2)
            pos_x += 1
            if moving == 1:
                moving = 3
            else:
                moving = 1
        

print(sum)