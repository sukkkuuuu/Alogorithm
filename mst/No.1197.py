# 최소 스패닝 트리
import sys,heapq
input = sys.stdin.readline

v, e = map(int,input().split())

graph = [[] for _ in range(v+1)]
visited = [0] * (v+1)
que = [[0,1]]
weight,count = 0,0

for _ in range(e):
    a,b,c = map(int,input().split())
    # a -> b로 가는 가중치 c 
    # b -> c로 가는 가중치 c 
    graph[a].append([c,b])
    graph[b].append([c,a])
    
while que:
    # 그래프 다 연결되면 탈출
    if count == v: break
    w,c_node = heapq.heappop(que)
    if not visited[c_node]:
        visited[c_node] = 1
        weight += w
        count +=1
        for neighbor in graph[c_node]:
            heapq.heappush(que,neighbor)
print(weight)