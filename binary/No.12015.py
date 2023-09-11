# 가장 긴 증가하는 부분 수열 2
import sys
input = sys.stdin.readline

n = int(input())

A = list(map(int, input().split()))

LIST = [A[0]]


def binary(N):
    L, R = 0, len(LIST) -1

    while(L <= R):
        mid = (L+R)//2
        if LIST[mid] == N:
            return mid
        elif LIST[mid] < N:
            L = mid+1
        else: R = mid -1
    return L

for i in A:
    if LIST[-1] < i:
        LIST.append(i)
    else:
        idx = binary(i)
        LIST[idx] = i
print(len(LIST))