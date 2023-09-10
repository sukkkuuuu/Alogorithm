# 공유기 설치
import sys
input = sys.stdin.readline

N, C = map(int,input().split())

homes = [int(input()) for _ in range(N)]
homes.sort()

L, R = 1, homes[-1] - homes[0] # 제일 짧은 거리랑, 제일 먼 거리
result = 0
while( L <= R):
    mid = (L+R)//2 # 현재 공유기 사이의 간격
    count = 1 # 공유기 설치 개수
    current = homes[0] # 현재 집의 위치
    diff = R

    # 간격을 mid(공유기 잡히는 거리)를 기준으로 잡고 mid 두 집 사이의 거리가 mid보다 크면 거기에 공유기를 설치하는 거임
    # 작으면 공유기 설치할 필요 없음, 그리고 설치한 지점부터 다시 공유기 안잡히는 곳까지 공유기 설치하러 갈거임
    for i in range(1,N):
        if homes[i] - current >= mid:
            diff = min(diff, homes[i] - current) # 가장 인접한 공유기 사이의 거리, 이거는 짧아야함 그래서 min
            count+=1
            current = homes[i]
    
    # 공유기 설치 개수가 3보다 크거나 같으면 공유기 사이의 거리(mid)가 넓은게 이유라서 mid를 줄이기 위해 L = mid + 1해준다
    if count >= C:
        L = mid + 1
        result = max(diff, result) # 위의 조건 만족하고 공유기 사이의 거리가 최대인 경우

    # 이거는 반대로 공유기 설치 개수가 부족해서 공유기 사이의 거리를 좁혀야함
    else:
        R = mid - 1

print(result)