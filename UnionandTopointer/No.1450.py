# 냅색문제
import sys
input = sys.stdin.readline

n, weight = map(int,input().split())

g = list(map(int,input().split()))

# C가 넘지 않게 가방에 물건 넣을 수 있는 경우의 수, 0포함
count = 1


