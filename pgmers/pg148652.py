# 프로그래머스 연습문제 유사칸토어비트열
# https://school.programmers.co.kr/learn/courses/30/lessons/148652

# map, reduce 사용으로 짧은코드지만 시간초과 발생

# TRY1
# from functools import reduce
# def solution(n, l, r):
#     curbits=str(1)
#     # print(type(curbits))
#     for i in range(1,n+1) :
#         curbits = reduce( lambda a,b:a+b ,map(lambda x : '11011' if x=='1' else '00000',curbits))
#         # print(f'curbits={curbits}')
#     return curbits[l-1:r].count('1')

# TRY2
# queue 를 이용한 방법 역시 시간초과
from collections import deque
def solution(n, l, r):
    tot_count = 5**n
    q = deque()
    q.append( (1,tot_count) )
    while q :
        if q[0][1] == 1 :
            break
        s,c = q.popleft()
        count = c // 5
        q.append((s,count))
        q.append((s+count,count))
        q.append((s+(count*3),count))
        q.append((s+(count*4),count))
    ans = len([ _ for s,_ in q if s in range(l,r+1)])
    return ans

# TRY 3
# 시간통과!!!
# n단계후의 리스트를 5조각내면 가운데조각은 0 나머지 조각은 1이라고 보고
# 각 조각의 Size가 1 이 될때 까지 처리하는 방법

from collections import deque
def solution(n, l, r):
    tot_count = 5**n
    q = deque()
    q.append( (1,tot_count) )
    while q :
        if q[0][1] == 1 :
            break
        s,c = q.popleft()
        count = c // 5
        if  s > l-count and s < r+count :
            q.append((s,count))
        if  s+count > l-count and s+count < r+count :
            q.append((s+count,count))
        if  s+(count*3) > l-count and s+(count*3) < r+count :
            q.append((s+(count*3),count))
        if  s+(count*4) > l-count and s+(count*4) < r+count :
            q.append((s+(count*4),count))
    return len(q)

print(solution(2,4,17))
