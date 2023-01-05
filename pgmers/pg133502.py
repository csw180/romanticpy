def solution(ingredient):
    answer = 0
    stck = []
    for v in ingredient :
        stck.append(v)
        if len(stck) >= 4 and  stck[-1]==1 and stck[-2] == 3 and stck[-3]==2 and stck[-4]==1 :
            stck.pop()
            stck.pop()
            stck.pop()
            stck.pop()
            answer+=1
    return answer

print(solution([2, 1, 1, 2, 3, 1, 2, 3, 1]))
print(solution([1, 3, 2, 1, 2, 1, 3, 1, 2]))