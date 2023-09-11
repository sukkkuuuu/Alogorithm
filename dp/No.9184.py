# 신나는 함수 실행
import sys
input = sys.stdin.readline

def w(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    elif a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)
    # 이부분을 추가해줘야지 속도가 빨라진다
    # dp안에 값이 있을 때 바로 출력하기 때문에, 이전에 했던 계산을 다시 하지 않아 되서 더 빠르게 돌아감
    if dp[a][b][c] :
        return dp[a][b][c]

    if a<b<c :
        dp[a][b][c] = w(a,b,c-1) + w(a,b-1,c-1) - w(a,b-1,c)
    else:
        dp[a][b][c] = w(a-1,b,c) + w(a-1,b-1,c) + w(a-1,b,c-1) - w(a-1,b-1,c-1)

    return dp[a][b][c]



dp = [[[0 for _ in range(21)] for _ in range (21)] for _ in range (21)]
while True:
    a,b,c = map(int, input().split())
    if a==-1 and b==-1 and c==-1:
        break
    print("w({}, {}, {}) = {}".format(a,b,c,w(a,b,c)))
