# 여행가자
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
    else: parent[a] = b

n = int(input())
m = int(input())
city = [list(map(int,input().split())) for _ in range(n)]

travel = list(map(int,input().split()))
parent = list(range(n))

for i in range(n):
    for j in range(n):
        if city[i][j] == 1:
            union(i,j)

answer = "YES"
for i in range(1,m):
    if parent[travel[i] - 1] != parent[travel[0] -1]:
        answer = "NO"
        break
print(answer)