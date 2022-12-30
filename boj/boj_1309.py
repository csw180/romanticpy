import sys

n = int(sys.stdin.readline())

dp = [1]*3
for i in range(1,n) :
    dp[0] , dp[1], dp[2] = dp[0]+dp[1]+dp[2],dp[0]+dp[2],dp[0]+dp[1]

print(sum(dp)%9901)