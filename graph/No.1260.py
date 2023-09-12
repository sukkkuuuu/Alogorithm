# DFS와 BFS
from collections import deque
import sys
input = sys.stdin.readline

N, M, V = map(int,input().split())

edges = [[] for _ in range(N+1)]
visited = [0] * (N+1)
bre,dep = [],[]
for _ in range(M):
    u,v = map(int,input().rstrip().split())
    edges[u].append(v)
    edges[v].append(u)

for i in range(N+1):
    edges[i].sort()

def DFS(R):
    visited[R] = 1
    dep.append(R)
    for neighbor in edges[R]:
        if not visited[neighbor]:
            DFS(neighbor)

def BFS(R):
    visited[R] = 1
    q = deque([R])
    bre.append(R)
    while q:
        p = q.popleft()
        for neighbor in edges[p]:
            if not visited[neighbor]:
                visited[neighbor] = 1
                bre.append(neighbor)
                q.append(neighbor)

DFS(V)
visited = [0] * (N+1)
BFS(V)
print(*dep)
print(*bre)