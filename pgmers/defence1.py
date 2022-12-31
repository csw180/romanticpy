# 프로그래머서 디펜스게임
# https://school.programmers.co.kr/learn/courses/30/lessons/142085?language=python3
# STACK 을 이용하여 소팅된상태로 유지를 하면서 최대값을 가져올수 있도록 구현
# 정확성은 PASS, 속도문제가 있음

def solution(n, k, enemy):
    klist = []
    stck = []
    tmpstk = []
    answer = -1

    for i,v in enumerate(enemy) :
        while(len(stck)> 0 and stck[-1] > v) :
            tmpstk.append(stck.pop());
        stck.append(v)
        while(len(tmpstk) > 0) :
            stck.append(tmpstk.pop());
        if  sum(stck) > n :
            if  len(klist) >= k :
                
                answer = i
                break
            else :
                klist.append(stck.pop())
        print(f'stck:{stck},tmpstk:{tmpstk},tlist:{klist}')
    if  answer==-1 :
        answer = len(enemy)
    return answer

# print(solution(7,3,[4, 2, 4, 5, 3, 3, 1]))
print(solution(6,4,[3, 3, 3, 3,4]))