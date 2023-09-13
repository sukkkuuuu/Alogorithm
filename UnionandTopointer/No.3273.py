# 두 수의 합
import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int,input().split()))
x = int(input())
L,R,count = 0, n-1,0
A.sort()
while L < R:
    if A[L] + A[R] > x:
        R-=1
    elif A[L] + A[R] < x:
        L+=1
    elif A[L] + A[R] == x:
            count+=1
            R-=1
print(count)