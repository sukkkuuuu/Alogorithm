# 알고리즘 수업 - 너비 우선 탐색 2
from collections import deque
import sys
input = sys.stdin.readline

def bfs(R):
    global c
    visited[R] = 1
    q = deque([R])
    while q:
        u = q.popleft()
        edges[u].sort(reverse = True)
        for neighbor in edges[u]:
            # 방문 안 했으면 실행
            if not visited[neighbor]:
                c+=1
                visited[neighbor] = c
                q.append(neighbor)

N, M, R = map(int,input().split())
c = 1
visited = [0] * (N+1)
edges = [[] for _ in range(N+1)]

for _ in range(M):
    u,v = map(int,input().split())
    edges[u].append(v)
    edges[v].append(u)

bfs(R)

for i in visited[1:]:
    print(i)