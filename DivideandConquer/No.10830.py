# 행렬 제곱

import sys
input = sys.stdin.readline
N, B = map(int,input().split())
C = 1000
A = [list(map(int, input().split())) for _ in range(N)]


# A * A 
def col(K, P):
    # 현재 들어온 배열들의 곱을 return 하기 위한 2차원 배열
    arr = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            s = 0
            for k in range(N):
                # N*N 행렬 곱셈
                s += K[i][k] * P[k][j]
            # 숫자가 커질 수 있어서 1000으로 나눠준다, 나머지 연산
            arr[i][j] = s % C
    return arr

def mult(B):
    # B 가 1이 아닐 경우에는 위에 col() 함수에서 나머지 연산(% C)을 해줬는데 1일 때는 아래의 과정을 거치지 않아서 따로 나머지 연산을 해줘야한다.
    if B == 1:
        for i in range(N):
            for j in range(N):
                A[i][j] %= C
        return A
    
    tmp = mult(B//2)
    
    if B % 2 == 0:
        # tmp * tmp
        return col(tmp, tmp)
    else:
        # (tmp * tmp) * A
        # a = col(tmp, tmp)
        return col(col(tmp, tmp), A)
        
result = mult(B)

for i in result:
    print(*i)
    