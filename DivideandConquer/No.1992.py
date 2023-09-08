# 쿼드트리
import sys
input = sys.stdin.readline

def div(N, x, y):
    color = Tree[x][y] # 현재 컬러색 
    # 각 사분면의 범위까지만 반복하기 위해서 x,y+N까지만 하는거임
    for i in range(x, x+N):
        for j in range(y, y+N):
            if color != Tree[i][j]:
                print("(",end='')
                div(N//2, x, y) # 좌상단
                div(N//2, x, y+N//2) # 우상단
                div(N//2, x+N//2, y) # 좌하단
                div(N//2, x+N//2, y+N//2) # 우하단
                print(")",end='')
                return
    if color == 0: print(0,end='')
    else: print(1, end='')
    
N = int(input())

Tree = [list(map(int, input().rstrip())) for _ in range(N)]
div(N, 0, 0)