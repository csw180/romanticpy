import sys

num = int(sys.stdin.readline().rstrip())

dp = [0]*(num+1)

for idx in range(2,num+1) :
    tmp = [dp[idx//i] for i in [2,3] if idx%i==0]
    tmp.append(dp[idx-1])
    dp[idx]= min(tmp)+ 1

print(dp[num])