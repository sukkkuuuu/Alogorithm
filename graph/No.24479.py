# 알고리즘 수업 - 깊이 우선 탐색 1
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
def dfs(R):
    global k
    visited[R] = k
    for neighbor in edges[R]:
        if not visited[neighbor] : 
            k+=1
            dfs(neighbor)

N, M, R = map(int,input().split())
k = 1
# edges
edges = [[] for _ in range(N+1)]
# U -> V 로의 간선은 있는데 V -> U로의 간선은 없다는 것 처럼 되어 있어서 양방향으로 만들어줘야함
for _ in range(M):
    u,v = map(int,input().split())
    edges[u].append(v)
    edges[v].append(u)

for i in range(N+1):
    edges[i].sort()

visited = [0] * (N+1)

# R: 시작 정점
dfs(R)
for i in range(1,N+1):
    print(visited[i])
