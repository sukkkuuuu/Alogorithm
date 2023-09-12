# # 특정한 최단 경로
import sys, heapq
input = sys.stdin.readline

n, e = map(int,input().split())
graph = [[]*(n+1) for _ in range(n+1)]
INF = sys.maxsize

for _ in range(e):
    a,b,c = map(int,input().split())
    # a <-> b 양방향 그래프에서 가중치가 c임을 표현함
    graph[a].append((b,c))
    graph[b].append((a,c))
# 반드시 지나야 하는 정점
v1, v2 = map(int,input().split())

def dij(start, to):
    # 최소 거리 저장할 배열
    distance = [INF for _ in range(n+1)]
    q = []
    # 가중치 0, 현재노드 K
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        W,node = heapq.heappop(q)
        if distance[node] < W: continue
        # i = 현재 node에서 갈 (다음노드, 가중치)를 나타냄
        for v, w in graph[node]:
            cost = w + distance[node]
            if distance[v] > cost:
                distance[v] = cost
                heapq.heappush(q, [distance[v], v])
    return distance[to]
# 이렇게 하면 v1, v2를 반드시 지나고 n을 가게 된다
# 1 -> v1으로 가는 경우와 1 -> v2로 가는 경우 두 가지 경우를 생각해줘야한다
path1 = dij(1, v1) + dij(v1, v2) + dij(v2, n)
path2 = dij(1, v2) + dij(v2, v1) + dij(v1, n)
if path1 >= INF and path2 >= INF:
    print(-1)
else: print(min(path1,path2))