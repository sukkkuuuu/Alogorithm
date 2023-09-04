import sys

n = int(sys.stdin.readline())
def recursion(s, left, right, count):
    count +=1
    if left >= right : 
        return 1, count
    elif (s[left] != s[right]): 
        return 0, count
    else : 
        return recursion(s, left+1, right-1, count)

def isPalindrome(s):
    count = 0
    return recursion(s, 0, len(s)-1, count)

for i in range(n):
    s = str(sys.stdin.readline().rstrip())
    k,v = isPalindrome(s)
    print(k,v)
