# 전력난
import sys

input = sys.stdin.readline


def find(a):
    if a != parent[a]:
        parent[a] = find(parent[a])
    return parent[a]


def union(a,b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b 

while 1 :
    m, n = map(int,input().split())
    if m == 0 and n == 0: 
        break
    parent = [i for i in range(m)]
    cost = 0

    graph = []
    for _ in range(n):
        x, y, z = map(int,input().split())
        graph.append((x, y, z))
    graph.sort(key=lambda x:x[2]) # z(가중치)를 기준으로 오름차순 정렬
    
    for g in graph:
        x, y, z = g
        if find(x) != find(y): # 부모노드 같은지 확인하고, 아니면 통일시켜줌
            union(x,y)
        else:
            cost += z
    print(cost)