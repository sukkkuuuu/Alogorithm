# 타임머신
import sys, heapq
input = sys.stdin.readline

N, M = map(int,input().split())

def bellman(R):
    distance[R] = 0
    for i in range(N):
        for j in range(M):
            node, next, w = bus[j][0], bus[j][1], bus[j][2]
            # 현재 노드가 INF 이면 접근 불가한 노드이기에 제외하고 생각해줘야한다
            if distance[node] != INF and distance[next] > distance[node] + w:
                distance[next] = distance[node] + w
                # 음수 사이클 잡아주는 구간
                if i == N-1:
                    return False
    return True

bus = []
INF = sys.maxsize
distance = [INF] * (N+1)

for _ in range(M):
    a,b,c = map(int,input().split())
    bus.append((a,b,c))

bo = bellman(1)

if not bo:
    print(-1)
else:
    for i in range(2, N+1):
        if distance[i] == INF:
            print(-1)
        else: print(distance[i])