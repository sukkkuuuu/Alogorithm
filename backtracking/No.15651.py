# N과 M(2) 백트래킹 문제 

import sys
input = sys.stdin.readline

def dfs():
    if len(s) == m : 
        print(' '.join(map(str,s)))
        return 
    else:
        for i in range(1,n+1):
            s.append(i)
            dfs()
            s.pop()

n,m = map(int,input().split())
s = []
dfs()