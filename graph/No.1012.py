# 유기농 배추
from collections import deque
import sys
input = sys.stdin.readline

def bfs(a, b):
    q = deque()
    q.append([a,b])
    # graph[a][b] = 0 # a,b 위치의 배추에 지렁이가 갔다는 의미 
    while q:
        x, y = q.popleft() # 배추가 있었던 좌표
        # graph[x][y] # a,b 위치의 배추에 지렁이가 갔다는 의미 
        # 상,하,좌,우에 배추가 심어져 있는지 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M: continue
            if graph[nx][ny] == 1:
                q.append([nx, ny])
                graph[nx][ny] = 0
    return 1
n = int(input())
for _ in range(n):
    M, N, K = map(int,input().split())
    graph = [[0 for _ in range(M)] for _ in range(N)]
    
    c = 0
    dx = [-1, 1, 0, 0] # 좌, 우
    dy = [0, 0, -1, 1] # 상, 하
    for _ in range(K):
        x, y = map(int,input().split())
        graph[y][x] = 1
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1:
                c+=bfs(i, j)
                
    print(c)
