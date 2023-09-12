# 동전 0
import sys
input = sys.stdin.readline

N, M = map(int,input().split())

coin = [int(input()) for _ in range(N)]
coin.sort(reverse=True)
result = 0

for i in coin :
		if M == 0: break
		result += M// i
		M %= i
print(result)