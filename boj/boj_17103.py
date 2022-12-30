import sys
case  = int(sys.stdin.readline().rstrip())
nums = []
for c  in range(case) :
    nums.append(int(sys.stdin.readline().rstrip()))
max_num = max(nums)
# 에라토스테네스의 체(소수구하기)
primeset = [True]*max_num
for i  in range(2,int(max_num**0.5)+1) :
    if  primeset[i] == True :
        for j in range(i*2,max_num,i) :
            primeset[j] = False

for _,v  in enumerate(nums) :
    print(sum([ 1 for i in range(2,(v//2)+1) if primeset[i] and primeset[v-i]]))