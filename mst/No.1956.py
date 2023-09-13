# 운동
import sys
input = sys.stdin.readline

v,e = map(int,input().split())

graph = [[sys.maxsize]*(v+1) for _ in range(v+1)]

for _ in range(e):
    a,b,c = map(int,input().split())
    graph[a][b] = c

for k in range(1, v+1):
    for i in range(1, v+1):
        for j in range(1, v+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

answer = sys.maxsize

for i in range(1, v+1):
    # 사이클은 출발지랑 도착지가 같기 떄문에 i->i를 비교해주면 된다
    answer = min(answer, graph[i][i])

if answer == sys.maxsize: print(-1)
else: print(answer)