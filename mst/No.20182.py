# 골목 대장 호석 - 효율성 1, 고쳐야함 못품
import sys, heapq
input = sys.stdin.readline

N, M, v1, v2, money = map(int,input().split())
INF = sys.maxsize
graph = [[] for _ in range(N+1)]
# 내는 요금을 저장하는 배열
costs = []
for _ in range(M):
    from_,to_,w = map(int,input().split())
    graph[from_].append((to_,w))
    graph[to_].append((from_,w))
    costs.append(w)

def dij(max_):
    # 수금하면서 낸 요금 저장
    distances = [INF] *(N+1)
    visited = [False] *(N+1)
    distances[v1] = 0
    visited[v1] = True
    pq = []
    heapq.heappush(pq, [0, v1])

    while pq:
        cost, node = heapq.heappop(pq)
        visited[cost] = True
        if distances[node] < cost: continue

        for next, ncost in graph[node]:
            if distances[next] > ncost + cost and ncost <= max_:
                # 간선 비용이 제한 비용 이내면 이동 가능
                distances[next] = ncost + cost
                heapq.heappush(pq, [ncost + cost, next])
    return False
#   사용 가능한 c원 이하로 b에 도착할 수 있다면 INF가 아닌 값 리턴

costs.sort()
L,R = -1, 21
answer = INF
while (L + 1 < R):
    mid = (L+R) // 2
    if (dij(mid)):
        R = mid
    else: L = mid
if answer == INF:print(-1)
else: print(answer)