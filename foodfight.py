# https://school.programmers.co.kr/learn/courses/30/lessons/134240
# 프로그래머서 연습문제 푸트파이터대회

def solution(food):
    answer = ''
    for i,v in enumerate(food):
        if i==0 :
            continue
        answer+=str(i)*(v//2)
        # print(f'answer={answer}')

    return answer+"0"+answer[::-1]

print(solution([1, 3, 4, 6]))