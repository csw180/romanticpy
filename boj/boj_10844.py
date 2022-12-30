import sys

def dpf(a,b) :
    result = 0
    if  a < 0 or a > n-1 or b < 0 or b > 9: result = 0
    else :
        result = dp[a][b]
    return result

n  = int(sys.stdin.readline().rstrip())
dp = [[0 for _ in range(10)] for _ in range(n)]
for i in range(1,10) :
    dp[0][i] = 1

# print('init' ,dp)
for i in range(1,n) :
    for j in range(10) :
        dp[i][j] = (dpf(i-1,j-1)+dpf(i-1,j+1)) 
    # print(dp)
# print('last',dp)
print(sum(dp[-1])%1000000000)