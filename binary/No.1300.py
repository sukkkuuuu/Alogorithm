# K 번째 수
import sys
input = sys.stdin.readline

n = int(input())
K = int(input())

L,R = 1,K
while(L<=R):
    mid = (L+R)//2
    tmp = 0

    for i in range(1, n+1):
        tmp += min(mid//i, n)
    if tmp >= K:
        answer = mid
        R = mid-1
    else: L = mid+1
print(answer)