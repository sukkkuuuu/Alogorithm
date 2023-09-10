# 곱셈
# 분할정복 문제라서 제곱된 수를 쪼개는 방식으로 접근했어야 하는 문제였다.
import sys
input = sys.stdin.readline

A, B, C = map(int, input().split())

def div(a,b):
    if b == 1:
        return a % C
    temp = div(a, b//2)
    # 짝수일 때 나눗셈 분배법칙
    if b % 2== 0:
        return temp*temp % C
    # 홀수 일 때 나눗셈 분배법칙
    else:
        return temp*temp*a%C
print(div(A,B))

# 아래와 같이 하면 숫자가 커졌을 때 런타임에러가 뜸 결과적으로 잘못 접근한 방법이다.
# def div(n):
#     global A, C
#     if n != 1:
#         # 나누는 수보다 나눠지는 수가 작을 때, A < C 
#         if A % C == A : 
#             A = A**2
#             div(n-1)
#         else:
#             A %= C
#             div(n-1)
#     else: return
# div(B)
# print(A)