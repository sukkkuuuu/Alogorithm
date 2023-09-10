# 숫자 카드 2
import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int,input().split()))
M = int(input())
B = list(map(int,input().split()))

A.sort()

def binary(A, L, R, x):
    if L > R: return 0 
    mid = (L+R)//2 if (L+R) % 2 == 0 else ((L+R)//2)+1 
    if A[mid] == x: 
        return cnt.get(x) # 해당 x에 대한 value를 return
    if A[mid] < x:
        return binary(A, mid+1, R, x)
    else:
        return binary(A, L, mid-1, x)
    
cnt = {}
for i in A:
    if i in cnt:
        cnt[i] +=1
    else: cnt[i] = 1
for x in B:
    a = binary(A, 0, len(A)-1,x)
    print(a, end=' ')

# binary_search 사용안하고 문제 푸는 방법
# for i in B:
#     if i in cnt:
#         print(cnt[i], end= ' ')
#     else: print(0, end=' ')