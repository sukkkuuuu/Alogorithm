# RGB 거리
import sys
input = sys.stdin.readline

n = int(input())

dp = [list(map(int,input().split())) for _ in range(n)]
for i in range(1,n):
    # 빨간집
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) +dp[i][0]
    # 파란집
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) +dp[i][1]
    # 초록집
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) +dp[i][2]

print(min(dp[n-1]))