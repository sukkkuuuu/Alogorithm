# 단지번호붙이기
from collections import deque
import sys
input = sys.stdin.readline

N = int(input())

graph = [list(map(int, input().rstrip())) for _ in range(N)]
aprt = []
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
def bfs(a, b):
    # x,y 좌표를 큐에 담음 
    q = deque()
    q.append([a,b])
    # x,y 좌표의 집이 큐에 들어가서 1 -> 0으로 바꿔줌 
    graph[a][b] = 0
    count = 1
    while q:
        x, y = q.popleft()
        graph[x][y] = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 범위 초과
            if nx < 0 or nx >=len(graph) or ny < 0 or ny >= len(graph): continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                q.append([nx, ny])
                count +=1
    return count


for i in range(N):
    for j in range(N):
        # 집이 있는 곳의 x,y 좌표
        if graph[i][j] == 1:
            aprt.append(bfs(i, j))
aprt.sort()
print(len(aprt))
for a in aprt:
    print(a)
