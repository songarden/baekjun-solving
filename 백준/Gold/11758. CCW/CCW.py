import sys

p1 = list(map(int,sys.stdin.readline().split()))
p2 = list(map(int,sys.stdin.readline().split()))
p3 = list(map(int,sys.stdin.readline().split()))


def ccw(p1, p2, p3):
    # 벡터 (p2 - p1)와 벡터 (p3 - p1) 계산
    vector1 = (p2[0] - p1[0], p2[1] - p1[1])
    vector2 = (p3[0] - p1[0], p3[1] - p1[1])

    # 외적 계산
    cross_product = vector1[0] * vector2[1] - vector1[1] * vector2[0]

    # 결과에 따라 방향성 판별
    if cross_product > 0:
        return 1
    elif cross_product < 0:
        return -1
    else:
        return 0

print(ccw(p1,p2,p3))