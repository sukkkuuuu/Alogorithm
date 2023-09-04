import sys
input = sys.stdin.readline

def pattern(N):
    if N == 3: return ["***","* *","***"]

    arr = pattern(N//3)
    stars = []
    
    # N == 3 일 때 return 되는 값들이 arr에 들어간다
    # 정사각형을 9 등분으로 나눠서 생각하면 편함 1~9째 칸에 N/3 패턴을 집어넣지만 5 번째 칸만 빈 칸이 되도록 한다 
    # 1~3번째 칸
    for i in arr:
        stars.append(i*3)
    # 4~6번째 칸, 5번째 칸은 빈칸 ' '*(N//3)
    for i in arr:
        stars.append(i+' '*(N//3)+i)
    # 7~9번째 칸,
    for i in arr:
        stars.append(i*3)
    return stars

N = int(input())

# 배열로 들어가있는 문자열을 하나씩 한 줄에 쓰기 위해서 '\n'.join() 사용 
print('\n'.join(pattern(N)))