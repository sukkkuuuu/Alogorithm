# 랜선 자르기
import sys
input = sys.stdin.readline

K, N = map(int,input().split())

A = [int(input()) for _ in range(K)]
L, R = 1, max(A) # 랜선의 처음과 끝 위치 (길이라고 생각하면 좋을듯), 왜 1부터 하냐면 랜선의 길이가 1보다 크니까

while (L <= R):
    print(L, end='-')
    print(R,end=' ')
    mid = (L+R)//2 # 제일 긴 랜선의 길이를 반으로 
    lines = 0 # 랜선 수
    for i in A:
        lines += i//mid # 분할된 랜선 수

    # 랜선의 개수가 분기점이 된다, 최대값을 찾는거라서 while문을 탈출 할 때까지 계속 해줘야한다.
    # 분할된 랜선 수가 내가 필요한 랜선 수 보다 많거나 같다면, 제일 짧은 길이의 값을 mid+1로 수정한다
    if lines >= N: 
        L = mid+1
    # 분할된 랜선 수가 내가 필요한 랜선 수 보다 작다면, 제일 긴 길이의 값을 mid-1로 수정 
    else: R = mid-1

print(R)