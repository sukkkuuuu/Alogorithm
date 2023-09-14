# 공항
import sys
input = sys.stdin.readline

g = int(input())
p = int(input())

# 들어오는 비행기 번호
airplane = [int(input()) for _ in range(p)]

# 번호에 맞는 게이트에 도킹시켜야함
# 1. 게이트가 활성화 되어있는 지 판단 root로드를 게이트 번호로 하자
# 2. 사용한 게이트는 비활성화로 만들어준다 root 노드를 0으로

gate = [i for i in range(g+1)]



def find(a):
    if a != gate[a]:
        gate[a] = find(gate[a])
    return gate[a]

def union(a,b):
    a = find(a)
    b = find(b)
    if a < b:
        gate[b] = a
    else: gate[a] = b
count = 0
for i in airplane:
    a = find(i)
    # 게이트가 비활성화 되어있다면
    if a == 0 :
        break
    # 현재 게이트를 사용하면 비활성화 하기 위해서 사용
    # a = 1, a-1 = 0 이라서 union(a,a-1)을 하면 1번 게이트가 비활성화(0이) 된다
    union(a,a-1)
    count+=1
print(count)