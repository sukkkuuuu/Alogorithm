# N과 M(1) 백트래킹 문제 
# 자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.
# 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열

import sys
input = sys.stdin.readline

def dfs():
    if len(s) == m : 
        # join은 str 상태인 것을 사용할 수 있기에 int를 str으로 바꿔줘서 출력해야한다
        print(' '.join(map(str,s)))
        return 
    else:
        for i in range(1,n+1):
            # 특정 숫자를 방문 했을 때 해당 숫자 두 번 접근 안하게 하기 위해서 
            if visited[i] : continue
            # 처음 방문 했을 때
            visited[i] = True
            s.append(i)
            dfs()
            # 다른 값을 넣어주기 위해 스택에 쌓인 값을 뺴준다
            s.pop()
            # 해당 숫자를 뺏기에 방문하지 않은 상태로 만들어준다
            visited[i] = False

n,m = map(int,input().split())
# 수열들을 저장할 스택
s = []
# 방문 여부를 확인할 배열 n+1을 해주는 건 배열 값이랑, index를 1~n로 사용하기 위해서
visited = [False] *  (n+1)
dfs()