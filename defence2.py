# 프로그래머서 디펜스게임
# https://school.programmers.co.kr/learn/courses/30/lessons/142085?language=python3
# heapq 최소값 이진트리 자료구조 이용한 방법
# 정확성, 속도 모두만족

import heapq

def solution(n, k, enemy):
    maxheap=[]
    kcnt=0
    heapsum=0
    answer = -1
    for i,v in enumerate(enemy) :
        heapq.heappush(maxheap,-v)
        heapsum+=-v
        if  heapsum < -n and len(maxheap) > 0 :
            if kcnt >= k :
                answer = i
                break
            else : 
                tmp = heapq.heappop(maxheap)
                heapsum-=tmp
                kcnt+=1
        # print(f'maxheap=[{maxheap}],kcnt=[{kcnt}],heapsum=[{heapsum}]')
    if answer==-1 :
       answer = len(enemy)        
    return answer

print(solution(7,3,[4, 2, 4, 5, 3, 3, 1]))
print(solution(2,4,[3, 3, 3, 3]))

