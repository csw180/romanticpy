import sys
n  = int(sys.stdin.readline().rstrip())
nums  = list(map(int,sys.stdin.readline().rstrip().split(" ")))

dp = [0 for i in range(n)]
for i in range(n):
    for j in range(i):
        if nums[i] > nums[j] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i] += nums[i]

print(max(dp))
