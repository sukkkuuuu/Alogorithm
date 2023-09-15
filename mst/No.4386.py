# 별자리 만들기
import sys,heapq,math
input = sys.stdin.readline

n = int(input())
visited = [0] * (n+1)
# 별의 2차원 좌표 [x,y]
stars = [list(map(float,input().split())) for _ in range(n)]
distance,count = 0,0
que = [[0,1]]
graph = [[] for _ in range(n+1)]

# 한 별에서 모든 다른 별로 가는 거리 저장, 자기자신으로 가는 거리는 0나옴
def stars_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

for i in range(n):
    # 자기자신의 거리는 0이기 때문에 자기자신을 제외하려고 i+1부터 시작 
    for j in range(i+1,n):
        # 별 i의 x,y 좌표
        x1, y1 = stars[i]
        # 별 j의 x,y 좌표
        x2, y2 = stars[j]
        # 별 i,j의 거리
        dis = stars_distance(x1, y1, x2, y2)

        # 별 i -> j 까지의 거리 dis
        graph[i].append([dis,j])
        graph[j].append([dis,i])

        
while que:
    w, c_node = heapq.heappop(que)
    if count == n: break
    if not visited[c_node]:
        visited[c_node] = 1
        distance += w
        count += 1
        for neighbor in graph[c_node]:
            heapq.heappush(que, neighbor)        
print('{:.2f}'.format(distance))
