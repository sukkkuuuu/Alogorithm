# 네트워크 연결
import sys,heapq
input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)
weight, count = 0, 0
que = [[0,1]]

for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append([c,b])
    graph[b].append([c,a])

while que:
    if count == n: break
    w, c_node = heapq.heappop(que)
    if not visited[c_node] : 
        visited[c_node] = 1
        weight += w
        count +=1
        for neighbor in graph[c_node]:
            heapq.heappush(que,neighbor)

print(weight)