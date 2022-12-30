import sys
n  = int(sys.stdin.readline().rstrip())

dp = [[0 for _ in range(n+1)] for _ in range(3)]

nums = []
nums.append(0)
for i in range(0,n) :
    nums.append(int(sys.stdin.readline().rstrip()))

for i in range(1,n+1) :
    dp[0][i] = max(dp[0][i-1],dp[1][i-1],dp[2][i-1])
    dp[1][i] = dp[0][i-1] + nums[i]
    dp[2][i] = dp[1][i-1] + nums[i]
#dp[0],dp[1],dp[2] 는 각각 i번째 잔을 
# 0:안먹고 스킵하는경우
# 1:먹긴하는데 직전 잔을 안먹은 경우
# 2:먹긴하는데 직전 잔도 먹어서 연거퍼 2번 먹게 되는경우

print(max(dp[0][n],dp[1][n],dp[2][n]))
