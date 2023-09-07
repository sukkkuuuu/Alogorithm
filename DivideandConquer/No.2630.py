import sys
input = sys.stdin.readline

def div(x,y,N):
    global white, blue

    color = arr[x][y]

    for i in range(x,x+N):
        for j in range(y, y+N):
            if color != arr[i][j]:
                # 좌상단, 1사분면
                div(x,y,N//2)
                # 우상단, 2사분면
                div(x,y+N//2,N//2)
                # 좌하단, 3사분면
                div(x+N//2,y,N//2)
                # 우하단, 4사분면
                div(x+N//2,y+N//2,N//2)
                return
    if color == 0 : white +=1
    else: blue += 1

N = int(input())

arr = [list(map(int,input().split())) for _ in range(N)]
white, blue = 0, 0
div(0,0,N)
print(white)
print(blue)