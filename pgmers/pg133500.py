def solution(n, lighthouse):
    answer = 0
    ajlst = []
    for _ in range(n+1) :
        ajlst.append(list())
    
    for v  in lighthouse:
        ajlst[v[0]].append(v[1])

    print(ajlst)
    return answer


solution(8,[[1, 2], [1, 3], [1, 4], [1, 5], [5, 6], [5, 7], [5, 8]])