import sys
input = sys.stdin.readline

n = int(input())
# dat, rup, rdown은 열, 우상향 대각선, 우하향 대각선 각 위치의 중복을 체크해줄 배열
dat = [0] * n
rup = [0] * (2*n-1)
rdown = [0] * (2*n-1)
cnt = 0

def func(level):
    global cnt
    # 마지막 행까지 도달하면 카운트
    if level == n:
        cnt += 1
        return
        
    for i in range(n):
    	# 열 중복체크, dat[열]
        if dat[i] == 1: continue
        # 우상향 대각선 중복체크, rup[행+열]
        if rup[level + i] == 1: continue
        # 우하향 대각선 중복체크, rdown[(행-열)+(n-1)]
        if rdown[(level - i) + (n-1)] == 1: continue
        
        # 모두 중복이 아니라면 1체크 후, 
        rup[level + i] = 1
        rdown[(level - i) + (n-1)] = 1
        dat[i] = 1
        
        # 다음 행 함수 호출
        func(level + 1)
        
        # return하면 다시 0으로 갱신
        dat[i] = 0
        rup[level + i] = 0
        rdown[(level - i) + (n-1)] = 0

func(0)
print(cnt)


# 아래의 방법은 시간 초과 발생함
# import sys
# input = sys.stdin.readline

# # 상하좌우, 대각선에 퀸 위치해 있는지 확인
# # nqueen에서 상하를 판별하지 않는데 그 이유는 한 줄에 하나의 퀸이 반드시 들어가야하기 때문에 신경쓰지 않는다, 트리를 그리면 row 단위로 노드를 뻗어나가서 신경쓰지 않는다고 보면 된다
# def check(n):

#     for i in range(n):
#         # 좌우, 대각선에 퀸 있을 경우
#         # 좌우 검사(board[n] == board[i]) 현재 퀸의 열(column) 위치와 기존에 적재된 퀸 중 특정 퀸의 열(column)위치가 같은지 확인 
#         # 대각선 검사(n-i == abs(board[n] - board[i]) => (현재 퀸의 raw - 기존 퀸의 raw)가 |현재 퀸의 column - 기존 퀸의 column|과 같은지 확인, 그림을 그려보면 이부분이 대각선이 된다
#         if (board[n] == board[i]) or (n-i == abs(board[n] - board[i])):
#             return False
#     return True 

# def nqueen(depth):
#     global count
    
#     # depth가 num일 때 모든 퀸을 다 놓은 것이라 판단
#     # depth는 행(row, 가로)를 의미한다
#     if depth == num:
#         count+=1

#     # depth별 반복문
#     for i in range(num):

#         # (depth,i) 위치에 퀸 올리기. depth는 row, i는 column임
#         board[depth] = i

#         # 상하좌우, 대각선에 퀸이 위치하는지 확인해줘야함
#         if check(depth):
#             nqueen(depth+1)

# num = int(input())
# # index는 row(세로줄)를 의미하고, value는 column(가로줄)를 의미한다
# board = [0] * num
# count = 0 
# nqueen(0)

# print(count)