# 프로그래머스 연습문제 우박수열 정적분
# https://school.programmers.co.kr/learn/courses/30/lessons/134239

def solution(k,ranges) :
    series =[k]
    areas = [0]
    while ( k != 1 ) :
        if  k%2==1 :
            k=3*k+1
        else :
            k=k//2
        areas.append( (series[-1] + k) / 2)
        series.append(k)
    # print(f'series={series}')
    # print(f'areas={areas}')

    result = []
    for t in ranges:
        if t[0]+1 > len(areas)+t[1] :
            result.append(-1.0)
        else :
            result.append(sum(areas[t[0]+1:len(areas)+t[1]]))
        # print(t[0]+1,len(areas)+t[1])
    # print(f'result={result}')
    return result
    
solution(5,[[0,0],[0,-1],[2,-3],[3,-3]]	)    