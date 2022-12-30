import sys
n  = int(sys.stdin.readline().rstrip())
nums  = list(map(int,sys.stdin.readline().rstrip().split(" ")))
nums_rev = nums[::-1]

dp_forw = [0  for _ in range(n)]
dp_bckw = [0  for _ in range(n)]

dp_forw[0] = 1
dp_bckw[0] = 1

for i in range(1,n) :
    for j in range(i):
        if  nums[j] < nums[i]  and dp_forw[j] > dp_forw[i] :
            dp_forw[i] = dp_forw[j]
        if  nums_rev[j] < nums_rev[i]  and dp_bckw[j] > dp_bckw[i] :
            dp_bckw[i] = dp_bckw[j]            
    dp_forw[i] +=1
    dp_bckw[i] +=1

print(max([sum(i)-1 for i in zip(dp_forw,dp_bckw[::-1])] ))