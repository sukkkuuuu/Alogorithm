# 회의실 배정
import sys
input = sys.stdin.readline

n = int(input())

com = [list(map(int,input().split())) for _ in range(n)]

com.sort(key = lambda x:(x[1],x[0])) # com[0] 를 기준으로 오름차순 정렬

count = 1
finish = com[0][1]
for i in range(1,n):
    if finish <= com[i][0]:
        count +=1
        finish = com[i][1]
print(count)