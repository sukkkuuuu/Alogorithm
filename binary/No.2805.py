# 나무 자르기
# 랜선 자르기 1654 문제랑 비슷했다.
import sys
input = sys.stdin.readline

N, M = map(int,input().split())

tree = list(map(int,input().split()))
tree.sort()
D, H = 1, max(tree)
while(D <= H):
    mid = (D+H)//2
    trees = 0
    for i in tree:
        # 음수일 때는 더하지 않게
        if i-mid > 0 :
            trees += i-mid
    if trees == M:
        H = mid
        break
    if trees >= M:
        D = mid+1
    else: H = mid-1
print(H)

