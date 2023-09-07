import sys 
input = sys.stdin.readline

N = int(input())
people = [list(map(int,input().split())) for _ in range(N)]
visited = [False for _ in range(N)]
INF = 2147000000
min_ = INF

def divide_team(depth,idx):
    global min_
    # N명이 있을 때 팀은 N//2 명으로 구성되기 때문에 depth == N//2 일 때 가지치기 시작
    if depth == N//2:
        start,link =0, 0
        for i in range(N):
            for j in range(N):
                if visited[i] and visited[j]:
                    start += people[i][j]
                elif not visited[i] and not visited[j]:
                    link += people[i][j]
        min_ = min(min_, abs(start-link))
        return
    for i in range(idx, N):
        if not visited[i] :
            visited[i] = True
            divide_team(depth+1,i+1)
            visited[i] = False

divide_team(0,0)
print(min_)