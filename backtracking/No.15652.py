# N과 M(2) 백트래킹 문제 

import sys
input = sys.stdin.readline

def dfs():
    if len(s) == m : 
        print(' '.join(map(str,s)))
        return 
    else:
        for i in range(1,n+1):
            if len(s) != 0 and i < s[len(s)-1]: continue
            s.append(i)
            dfs()
            s.pop()

n,m = map(int,input().split())
s = []
dfs()