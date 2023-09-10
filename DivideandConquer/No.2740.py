# 행렬 곱셈
import sys
input = sys.stdin.readline

N, M = map(int,input().split())

A = [list(map(int,input().split())) for _ in range(N)]

m, K = map(int,input().split())

B = [list(map(int,input().split())) for _ in range(m)]

C = [[0 for _ in range(K)] for _ in range(N)]

# 최대 10**6 까지...
for i in range(N):
    for j in range(M):
        for k in range(K):
            C[i][k] += A[i][j] * B[j][k]

for i in C:
    print(*i)