import sys

n  = int(sys.stdin.readline().rstrip())
dp = [[0 for _ in range(n+2)] for _ in range(n+1)]

for c in range(n) :
    nums = list(map(int,sys.stdin.readline().rstrip().split(' ')))
    for i in range(len(nums)) :
        dp[c+1][i+1] = nums[i]

for c in range(2,n+1) :
    for i in range(1,c+1) :
        dp[c][i] += max(dp[c-1][i-1],dp[c-1][i])

print(max(dp[n]))
