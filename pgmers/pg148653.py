# 프로그래머스 연습문제  마법의엘리베이터
# https://school.programmers.co.kr/learn/courses/30/lessons/148653
'''
예를 들어 91 이라면
91을 에서 -10을 9번 눌러서 곧장내려가는 경우도 있겠지만
-100을 한번누르고 9(100에대한 91의 보수)만큼 꺼꾸로 돌아가는 경우가 있을것이다.
이렇게 곧바로 가는경우만 한번 지나져서 돌아가는 두가지 경우를 순회해서 남은층수를 
계속 줄여나가는 모든경우의 수를 조사해서 움직임이 적은것을 고르는 방식이다.
큐 (a,b) 
a: 움직임 누적 count
b: 더 조사해야할 남은 층수
'''
from collections import deque

def solution(story) :
    q = deque()
    unit = getUnit(story)
    d,m = divmod(story,unit)
    q.append((0,story))
    if story > unit*10-story:
        q.append((1,unit*10-story))
    print(q)

    anslst = []
    while q :
        c,s = q.popleft()
        if  s <= 5 :
            anslst.append(c+s)
            continue
        else :
            unit = getUnit(s)
            d,m = divmod(s,unit)
            q.append((c+d,m))
            if s > unit*10-s :
                q.append((c+1,unit*10-s))
        print(q)
    # print(f' last anslst= {anslst}')
    return min(anslst)

def getUnit(s) :
    cnt=0
    while s :
        s = s // 10
        cnt+=1
    return 10**(cnt-1)


print(f'input 91 = {solution(91)}')
print(f'input 81 = {solution(81)}')