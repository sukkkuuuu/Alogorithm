# 상근이의 여행
import sys
input = sys.stdin.readline

t = int(input())

def dfs(a, count):
    visited[a] = 1
    for node in graph[a]:
        if visited[node] == 0:
            count = (dfs(node,count+1))
    return count

for _ in range(t):
    n, m = map(int,input().split())
    graph = [[] for _ in range(n+1)]
    visited = [0] * (n+1)
    for _ in range(m):
        a,b = map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)
    print(dfs(1,0))
    
    # print(n-1)


        



