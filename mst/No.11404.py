# 플로이드
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
INF = sys.maxsize
graph = [[INF]*(n+1) for _ in range(n+1)]

for i in range(1,n+1):
    graph[i][i] = 0

for _ in range(m):
    a,b,c = map(int,input().split())
    # 시작 -> 도착으로 가는 노선이 여러개 있을 수 있어서 최소 값을 저장
    graph[a][b] = min(graph[a][b], c)

for k in range(1,n+1): # 경유지
    for i in range(1,n+1): # 출발지
        for j in range(1,n+1): # 도착지
            # 현재 저장된 i -> j로의 노선이 빠른지 경유지를 거쳐가는 i -> k -> j 빠른지 비교 
            graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])

for i in range(1,n+1):
    for j in range(1,n+1):
        if graph[i][j] == INF:
            print(0, end = ' ')
        else: print(graph[i][j], end=' ')
    print()