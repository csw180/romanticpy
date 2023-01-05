# 프로그래머스 연습문제 옹알이2
# https://school.programmers.co.kr/learn/courses/30/lessons/133499

def solution(babbling):
    answer = 0
    combi = ["aya", "ye", "woo", "ma"]
    for v in babbling :
        pos=0
        stack = []
        enable = False
        while (pos<=len(v)-1) :
            # print(f'pos={pos},pos+2:{v[pos:pos+2]},pos+3{v[pos:pos+3]}')
            if v[pos:pos+2] in combi and v[pos:pos+2] not in stack :
                stack.clear()
                stack.append(v[pos:pos+2])
                pos = pos + 2
                enable = True
                # print(f'stack={stack}')
            elif v[pos:pos+3] in combi and v[pos:pos+3] not in stack :
                stack.clear()
                stack.append(v[pos:pos+3])
                pos = pos + 3
                enable = True
                # print(f'stack={stack}')
            else :
                enable = False
                break
        if enable :
            answer +=1

    return answer


print(solution(["aya", "yee", "u", "maa"]))
print(solution(["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"]))

