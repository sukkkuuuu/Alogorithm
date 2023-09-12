# 바이러스
from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
M = int(input())

computers = [[] for _ in range(N+1)]
visited = [0] * (N+1)
count = 0

for _ in range(M):
    u, v = map(int,input().split())
    computers[u].append(v)
    computers[v].append(u)

def bfs(R):
    global count
    visited[R] = 1
    q = deque([R])
    q.append(1)
    while q:
        p = q.popleft()
        for neighbor in computers[p]:
            if not visited[neighbor]:
                count +=1
                visited[neighbor] = 1
                q.append(neighbor)

bfs(1)
print(count)