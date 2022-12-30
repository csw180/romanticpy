import sys
n  = int(sys.stdin.readline().rstrip())

def dp_v(n,dp) :
    if  n < 0 : return 0
    else :
        return dp[n]

dp = [1,1]
for i  in range(2,n+1) :
    dp.append(dp_v(i-1,dp) + dp_v(i-2,dp))

print(dp[-1]%10007)
