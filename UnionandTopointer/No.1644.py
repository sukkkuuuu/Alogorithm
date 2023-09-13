# 소수의 연속합
import sys
input = sys.stdin.readline

n = int(input())
a = [False,False] + [True] * (n-1)
prime = []

# 에라토스테네스의 체
for i in range(2,n+1):
    if a[i]:
        prime.append(i)
        for j in range(2*i, n+1,i):
            a[j] = False

count,left,right = 0, 0, 0

while 1:
    if right > len(prime): break
    sum_ = sum(prime[left:right])
    if sum_ == n:
        count+=1
        right+=1
    elif sum_ > n:
        left+=1
    else: right+=1
print(count)
