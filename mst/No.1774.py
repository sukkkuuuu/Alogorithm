# 우주신과의 교감
import sys,heapq,math
input = sys.stdin.readline

n, m = map(int,input().split())

def distance(x1, y1, x2, y2):
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)

graph = [[] for _ in range(n+1)]

gods = [list(map(int,input().split())) for _ in range(n)]
gods = [[]] + gods
conntect = set()
for _ in range(m):
    s1,s2 = map(int,input().split())
    # 양방향이라서 이렇게 해줌
    conntect.add((s1,s2))
    conntect.add((s2,s1))
# print(conntect)
for i in range(1,n+1):
    for j in range(i+1,n+1):
        x1, y1 = gods[i]
        x2, y2 = gods[j]
        dis = distance(x1, y1, x2, y2)
        if (i,j) in conntect:
            graph[i].append([0,j])
            graph[j].append([0,i])
            continue
        graph[i].append([dis,j])
        graph[j].append([dis,i])

# print(graph)
visited = [0] * (n+1)
que = [[0,1]]
cost = 0
count = 0
while que:
    if count == n: break
    w, c_node = heapq.heappop(que)
    if not visited[c_node]:
        visited[c_node] = 1
        cost+=w
        count +=1
        for neighbor in graph[c_node]:
            heapq.heappush(que,neighbor)
print('{:.2f}'.format(cost))