import sys

dp = [0 for _ in range(1000001)]
dp[1] = 1
dp[2] = 2
dp[3] = 4

for i in range(4,1000001) :
    dp[i] = ( dp[i-1] + dp[i-2] + dp[i-3] )  % 1000000009

n  = int(sys.stdin.readline().rstrip())

cases = []
for i in range(n) :
    cases.append(int(sys.stdin.readline().rstrip()))

for v in cases :
    print(dp[v] % 1000000009)
