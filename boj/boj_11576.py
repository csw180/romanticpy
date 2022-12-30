import sys

a,b = map(int,sys.stdin.readline().rstrip().split(" "))
n   = int(sys.stdin.readline().rstrip())
digit = list(map(int,sys.stdin.readline().rstrip().split(" ")))

d = sum( [v*(a**(n-i-1)) for i,v in enumerate(digit)] ) # a진수를 10진수로
result =[]                                              # 10진수로 b진수로
while  d != 0 :            
    result.append(d%b)
    d //= b
print(*result[::-1])