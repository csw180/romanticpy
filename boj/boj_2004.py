import sys

def nk(n,k) :
    count = 0
    i = 1
    while n >= k**i : 
        count += ( n // (k**i) )
        i +=1
    return count

# 요개 정답으로 돌아댕기는데 더 심플하긴 하나..
# 결과는 내가 만든거랑 같으나 어째 이해가좀 안됨
# 그냥 내가 만든걸로 ..쓰기로 
# def twoCount(n,k):
#     answer = 0
#     while n != 0:
#         n = n // k
#         answer += n
#     return answer
nums  = list(map(int,sys.stdin.readline().rstrip().split(' ')))
count2 = nk(nums[0],2) - nk(nums[1],2) -  nk(nums[0]-nums[1],2)
count5 = nk(nums[0],5) - nk(nums[1],5) -  nk(nums[0]-nums[1],5)

print(min(count2,count5))