# 숨바꼭질 3
# 0-1 bfs 알고리즘
from collections import deque
import sys
input = sys.stdin.readline

n, k = map(int,input().split())
visited = [-1] * 100001 # N의 최대 크기가 10만이라서 

q = deque([n])
visited[n] = 0
while q:
    current = q.popleft()

    # 현재 위치가 동생 위치일 경우 현재 위치 출력
    if current == k:
        # 이때까지 누적되어온 시간을 출력
        print(visited[current])
        break

    # 현재 위치의 범위와 이전 위치는 방문하지 않았을 때
    if 0 <= current-1 <= 100000 and visited[current-1] == -1:

        # 이전 위치에 지금까지 걸린 시간 + 1
        visited[current-1] = visited[current] + 1

        # 큐에는 이전 위치 담음
        q.append(current-1)

    # 현재 위치의 범위와 현재위치*2 위치는 방문하지 않았을 때
    if 0 <= current*2 <= 100000 and visited[current*2] == -1:

        # *2 위치에 지금까지 걸린 시간 + 0
        visited[current*2] = visited[current] + 0

        # 큐에 *2 위치 담음
        q.append(current*2)

    # 현재 위치의 범위와 다음 위치는 방문하지 않았을 때
    if 0 <= current+1 <= 100000 and visited[current+1] == -1:

        # 다음 위치에 지금까지 걸린 시간 + 1
        visited[current+1] = visited[current] + 1

        # 큐에 다음 위치 담음
        q.append(current+1)
# 순서를 +1이 맨 뒤에 와야하는 이유
# 동생보다 거리가 작음면 무조건 한 칸씩 움직여서 동생에게 가기 때문에 최단 시간이 걸릴 수가 없음 