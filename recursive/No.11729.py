import sys
input = sys.stdin.readline

def hanoi(n, from_, to_, by_):
    if n == 1: 
        arr.append(from_)
        arr.append(to_)
    else:
        hanoi(n-1,from_, by_, to_)
        arr.append(from_)
        arr.append(to_)
        hanoi(n-1,by_, to_, from_)

n = int(input())
arr = []
hanoi(n,1, 3, 2)
print(len(arr)//2)
for i in range(0,len(arr),2):
    print(arr[i], arr[i+1])
