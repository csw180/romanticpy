# 프로그래머서 연습문제 > 가장 가까운 같은글자
# https://school.programmers.co.kr/learn/courses/30/lessons/142086

def solution(s):
    answer = [0]*len(s)
    for i in range(len(s)) :
        for j in range(1,i+1) :
            if s[i]==s[i-j] :
                answer[i]=j
                break
        if answer[i]==0 :
            answer[i]=-1

    return answer


print(solution("banana"))
print(solution("foobar"))

