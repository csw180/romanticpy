import sys

dp =[0] * 3

n = int(sys.stdin.readline())
rgb = []
for c in range(n) :
    rgs_in = list(map(int,sys.stdin.readline().rstrip().split(" ")))
    rgb.append(rgs_in)

for i,v in enumerate(rgb) : dp[0],dp[1],dp[2] = min(dp[1],dp[2])+v[0],min(dp[0],dp[2])+v[1],min(dp[0],dp[1])+v[2]

print(min(dp))