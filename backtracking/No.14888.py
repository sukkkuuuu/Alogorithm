import sys
input = sys.stdin.readline

def oper(depth, total, plus, minus, mult, divide): 
    global max_, min_
    if depth == N:
        max_ = max(total, max_)
        min_ = min(total, min_)
        return
    if plus:
        oper(depth + 1, total + arr[depth], plus - 1, minus, mult, divide)
    if minus:
        oper(depth + 1, total - arr[depth], plus, minus - 1, mult, divide)
    if mult:
        oper(depth + 1, total * arr[depth], plus, minus, mult - 1, divide)
    if divide:
        # total / arr[depth]이렇게 하면 음수 나눗셈 할 때 몫이 소수점 아래로 떨어지면 더 작은 값을 반환해서 int(total / arr[depth]) 이렇게 써줘야지 원하는 값이 나온다
        # -10 나누기 3은 -3.3333... 이다.
        # // 연산자는 나누기 결과보다 작은 정수 중 가장 큰 정수인 -4를,
        # int() 연산자는 그냥 소수 부분을 버려서 -3을 결과로 갖는다.
        oper(depth + 1,  int(total / arr[depth]), plus, minus, mult, divide -1)

N = int(input())
arr = list(map(int,input().split()))
# +,-,*,% 연산자의 개수
operator = list(map(int,input().split()))
max_ = -sys.maxsize
min_ = sys.maxsize

oper(1, arr[0], operator[0],operator[1],operator[2],operator[3])

print(max_)
print(min_)