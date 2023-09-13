#부분합
import sys
input = sys.stdin.readline

n, s = map(int,input().split())

A = list(map(int,input().split()))
INF = sys.maxsize
min_,sum_,left, right = INF,0,0,0

while 1:
    if sum_ >= s:
        min_ = min(min_, right-left)
        sum_ -= A[left]
        left+=1
    elif right == n : break
    else:
        sum_+=A[right]
        right+=1
if min_ == INF: print(0)
else: print(min_)
