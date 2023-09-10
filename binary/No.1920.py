# 수 찾기
import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int,input().split()))

M = int(input())
B = list(map(int,input().split()))
# binary_search 이용
A.sort()
def binary(A, L, R, x):    
    if L > R: return 0
    mid = (L+R)//2 if (L+R) % 2 == 0 else ((L+R)//2)+1 
    if A[mid] == x: return 1
    if x >= A[mid]:
        return binary(A,mid+1, R, x)
    else:
        return binary(A, L, mid-1, x)
    
for x in B:
    print(binary(A, 0 ,len(A)-1, x))

# A를 list말고 set으로 받아서 풀 수도 있다. 이 경우가 더 빠름, set은 dict와 비슷한데 키 값만 가지고 있다.
# A = set(map(int,input().split()))
# for i in B:
#     print(1) if i in A else print(0)
