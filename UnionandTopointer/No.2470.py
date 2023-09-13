# 두 용액
import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int,input().split()))

left, right = 0, n-1
A.sort()
result = abs(A[left] + A[right])
save = [A[left], A[right]]

while left < right:
    sum_ = A[left] + A[right]
    if result > abs(sum_):
        result = abs(sum_)
        save = [A[left],A[right]]
        if result == 0:
            break
    if sum_ < 0:
        left += 1
    else: 
        right -= 1
print(save[0], save[1])