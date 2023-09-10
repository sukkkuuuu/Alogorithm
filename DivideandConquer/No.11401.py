# 이항계수
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
N, R = map(int,input().split())
C = 1000000007

# 재귀 사용하면 시간초과 뜸
def fac(n):
    result = 1
    for i in range(2, n+1):
        result = (result * i) % C
    return result

# n의 r승을 계산하는 함수, 여기서 분할정복 사용됨
# 거듭제곱 계산, B^p-2 % C 이부분을 계산하는 거임
# 10 ** 5 = (10**2) * (10**2) * 10 으로 표현하려고 하는 함수
def binomial(n,r):
    # n의 0승은 1
    if r == 0:
        return 1
    # n의 1승은 n
    if r == 1:
        return n

    tmp = binomial(n, r//2)

    if r % 2 :
        # 홀수 일 때
        return tmp * tmp * n % C
    else:
        # 짝수 일 때
        return tmp * tmp % C
       
top = fac(N) % C # n!
bottom = fac(N-R) * fac(R) # r!*(n-r)!

# 페르마의 소정리를 이용해서 나눗셈 분배법칙을 사용한다
# (A/B) % C = (A%C) * (B^p-2 % C) % C
# nCr = n! / r!*(n-r)! 위의 공식 적용해서 풀어야한다
print(top * binomial(bottom, C-2) % C)