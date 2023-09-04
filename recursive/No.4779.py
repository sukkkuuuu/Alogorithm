import sys
input = sys.stdin.readline

def slice(n):
    if n == 1: return '-'
    else:
        return slice(n//3) + ' '*(n//3) + slice(n//3)

while 1:
    try:
        n = int(input())
        k = slice(3**n)
        print(k)
    except: break