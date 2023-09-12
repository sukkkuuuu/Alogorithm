# 최단경로
import heapq
import sys
input = sys.stdin.readline

V, E = map(int,input().split())
K = int(input())
que = []
edges = [[]*(V+1) for _ in range(V+1)]
INF = sys.maxsize
# 최소 가중치 저장되어 있어있는 배열 
wi = [INF for _ in range(V+1)]
for _ in range(E):
    u,v,w = map(int,input().split())
    # u -> v 가는 가중치가 w이다 
    # edges[u] = (v,w)
    edges[u].append((v,w))

def dij(K):
    # index -> K 로의 가중치 0
    heapq.heappush(que,(0,K))
    wi[K] = 0
    while que:
        # w는 가중치, node는 현재 위치한 노드
        w,node = heapq.heappop(que)
        if wi[node] < w:
            continue
        for u in edges[node]:
            # 현재 가중치 + 다음 index로 가는대 필요한 가중치 u[1]을 더한다
            # u[0]는 다음 노드를 가르키고, u[1]는 다음 노드로 가는데 필요한 가중치
            cost  = w + u[1]
            # 다음 가중치까지 더한게 저장되어 있던 u->v로(다음 node까지) 가는데 걸리는 가중치보다 작으면 최소 값이 발견 된거라서 갱신해준다
            if cost < wi[u[0]]:
                wi[u[0]] = cost
                heapq.heappush(que, (cost,u[0]))

dij(K)
for i in range(1, V+1):
    if wi[i] == INF:
        print("INF")
    else: print(wi[i])