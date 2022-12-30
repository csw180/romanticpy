import sys
case  = int(sys.stdin.readline().rstrip())
prob = []
for c in range(case) :
    prob.append(int(sys.stdin.readline().rstrip()))

n = max(prob)
nums = [[0 for _ in range(n)] for _ in range(3)]
nums[0][0] = nums[0][2] = 1
nums[1][1] = nums[1][2] = 1
nums[2][2] = 1

for i in range(3,n) :
    nums[0][i] = (nums[1][i-1]+nums[2][i-1]) % 1000000009  #얼마나큰수가 들어오길레 % 안하면 메모리초과남
    nums[1][i] = (nums[0][i-2]+nums[2][i-2]) % 1000000009
    nums[2][i] = (nums[0][i-3]+nums[1][i-3]) % 1000000009

# for l in range(3) :
#     print(nums[l])
    
for c in range(case) :
    k =  prob[c]
    print((nums[0][k-1]+nums[1][k-1]+nums[2][k-1]) % 1000000009)