import sys
n  = int(sys.stdin.readline().rstrip())
nums  = list(map(int,sys.stdin.readline().rstrip().split(" ")))

dp = [0 for i in range(n)]
for i in range(n):
    for j in range(i):
        if nums[i] > nums[j] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i] += 1

max_dp = max(dp)
c = max_dp
result = []
for i in range(len(dp)-1,-1,-1) :
    if  dp[i] == c :
        result.append(nums[i])
        c -= 1

print(max_dp)
print(*result[::-1])
