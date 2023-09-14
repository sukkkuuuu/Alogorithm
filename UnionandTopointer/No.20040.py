# 사이클 게임
import sys
input = sys.stdin.readline

def find(a):
    if a != parent[a]:
        parent[a] = find(parent[a])
    return parent[a]

def union(a,b):
    a = find(a)
    b = find(b)
    if a == b:
        return
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n,m = map(int,input().split())
parent = [i for i in range(n)]


k = 0

for i in range(m):
    a,b = map(int,input().split())
    a = find(a)
    b = find(b)

    if a == b:
        k = i+1
        break
    union(a,b)
print(k)