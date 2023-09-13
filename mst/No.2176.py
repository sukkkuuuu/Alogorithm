# 합리적인 이동경로
import sys,heapq
input = sys.stdin.readline

n, m = map(int,input().split())
INF = 2147483647

graph = [[] for _ in range(n+1)]
distance = [INF]*(n+1)
dp = []
for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))
# 기본적인 다익스트라 알고리즘
def dij(s):
    distance[s] = 0 
    q = []
    heapq.heappush(q,(0,s))
    while q:
        cost, node = heapq.heappop(q)
        if distance[node] < cost :continue
        for next, w in graph[node]:
            c = distance[node] + w
            if distance[next] > c:
                distance[next] = c
                heapq.heappush(q,(distance[next], next))
dij(2)
print(graph)
print(distance)
# 다익스트라 알고리즘에서 구한 distance를 가지고 합리적인 경로 찾을거임 
def path(c_node):
    # 이 노드를 거친적이 없을 때 
    if dp[c_node] == 0:
        # 해당 노드의 이웃 노드들 확인
        for n_node, n_cost in graph[c_node]:
            # 현재 가중치값이, 다음 가중치값보다 크면 현재 횟수에 다음 노드의 횟수를 더한다?
            if distance[c_node] > distance[n_node]:
                # 이동 횟수를 추가해줌
                dp[c_node] += path(n_node)
        return dp[c_node]
    else: return dp[c_node]

# 횟수 저장하는 배열
dp = [0] * (n+1)
# 1 -> 2로 가는 거라서 아무 노드도 경유하지 않고 바로 2번 노드로 갈 수 있기 때문에 1(회)로 설정
dp[2] = 1
print(path(1))
print(dp)