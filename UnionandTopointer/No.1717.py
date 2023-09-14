# 집합의 표현
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

n,m = map(int,input().split())
parent = [0] *(n+1)
for i in range(n+1):
    parent[i] = i

def find(a):
    # 자기 자신이 루트면 자기자신 리턴
    if a == parent[a]: 
        return a
    # a의 루트노드 찾기
    pf = find(parent[a])
    parent[a] = pf # 부모 테이블 갱신
    return parent[a]

def union(a,b):
    # a,b의 루트노드를 찾아줘야한다
    a = find(a)
    b = find(b)
    if a == b:
        return 
    if a > b:
        parent[a] = b
    else:
        parent[b] = a

for _ in range(m):
    tf,a,b = map(int,input().split())
    if tf:
        f = find(a)
        k = find(b)
        if k == f: print("YES")
        else: print("NO")
    else: union(a,b)
