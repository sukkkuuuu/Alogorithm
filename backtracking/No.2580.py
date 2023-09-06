import sys
input = sys.stdin.readline

sdoku = [list(map(int,input().split())) for _ in range(9)]
zero = []
for i in range(9):
    for j in range(9):
        # boolean으로 판단할 경우 0 이외의 숫자는 1로 판단함
        if not sdoku[i][j]:
            zero.append((i,j))


def check(N, ny, nx):
    # 받은 좌료가 어느 위치에 있는지 확인, 전체를 9등분 했을 때의 위치를 판단하기 위해서
    x, y = (nx//3)*3, (ny//3)*3
    # 가로, 세로, 3*3칸 안에 없는 숫자를 찾아야한다

    for i in range(9):
        # 가로에 없는 숫자4
        if sdoku[ny][i] == N: return False

        # 세로에 없는 숫자
        if sdoku[i][nx] == N: return False

        # 3*3 칸에 없는 숫자, 세로 한줄에 가로 세개를 확인 해야하기에 i//3, i%3으로 차이를 준거임
        if sdoku[y + i // 3][x + i % 3] == N: return False

    return True

def dfs(depth):
    # 종결문
    if depth == len(zero):
        for i in range(9):
            print(*sdoku[i])
        exit(0)

    y, x = zero[depth]

    # 스도쿠에 넣을 숫자 
    for i in range(1,10):
        # 0인 숫자를 가진 좌표를 보낸다
        # 3가지 조건을 만족했을 때 실행
        if check(i, y, x):
            sdoku[y][x] = i
            dfs(depth+1)
            sdoku[y][x] = 0
dfs(0)