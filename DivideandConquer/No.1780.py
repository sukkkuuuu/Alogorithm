# 종이의 개수
import sys
input = sys.stdin.readline

N = int(input())

shape = [list(map(int,input().split())) for _ in range(N)]

def div(N, x, y):
    global zero, one, minus

    color = shape[x][y]

    for i in range(x, x+N):
        for j in range(y, y+N):
            # 색이 다를 때, 9등분 해야함
            if color != shape[i][j]:
                div(N//3, x, y)
                div(N//3, x, y+N//3)
                div(N//3, x, y+(N//3)*2)
                div(N//3, x+N//3, y)
                div(N//3, x+N//3, y+N//3)
                div(N//3, x+N//3, y+(N//3)*2)
                div(N//3, x+(N//3)*2, y)
                div(N//3, x+(N//3)*2, y+N//3)
                div(N//3, x+(N//3)*2, y+(N//3)*2)
                return
    if color == 0: zero+=1
    elif color == 1: one+=1
    else: minus+=1

zero, one, minus = 0, 0, 0
div(N,0, 0)
print(minus)
print(zero)
print(one)

