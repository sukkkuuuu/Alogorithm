# 친구 네트워크
import sys
input = sys.stdin.readline

n = int(input())

def union(a,b):
    a = find(a)
    b = find(b)
    if a == b:
        return friends[a]
    # b의 부모를 a로 바꾼다
    parent[b] = a
    # 그리고 a의 친구수에 b의 친구수를 더한다
    friends[a] += friends[b]
    return friends[a]

def find(a):
    if a != parent[a]:
        parent[a] = find(parent[a])
    return parent[a]

for i in range(n):
    F = int(input())
    parent = {}
    friends = {}
    for _ in range(F):
        A, B = map(str,input().split())
        if parent.get(A) == None:
            parent[A] = A
            friends[A] = 1
        if parent.get(B) == None:
            parent[B] = B
            friends[B] = 1
        print(union(A,B))
        