import sys
n = int(sys.stdin.readline().rstrip())
nums = list(map(int,sys.stdin.readline().rstrip().split(" ")))

sums = [0 for _ in range(n)]

sums[0] = nums[0]
for i,v in enumerate(nums) :
    if i == 0  : continue
    sums[i] = max( sums[i-1]+nums[i], nums[i])

print(max(sums))