import sys
nums = list(map(int,sys.stdin.readline().rstrip().split(' ')))
print( (nums[0]+nums[1]) % nums[2])
print( ((nums[0]%nums[2])+(nums[1]%nums[2])) % nums[2])
print( (nums[0]*nums[1]) % nums[2])
print( ((nums[0]% nums[2])*(nums[1]% nums[2])) % nums[2])
