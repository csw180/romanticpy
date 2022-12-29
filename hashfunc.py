def solution(data, col, row_begin, row_end):
    answer = 0
    data.sort(key=lambda a : (a[col-1],-a[0]))
    for i in range(row_begin,row_end+1) :
        mods = sum([j%i for j in data[i-1]])
        if i==row_begin :
            answer = mods
        else :
            answer = answer^mods
    # print(f'answer={answer},mods={mods}')
    return answer

print(solution([[2,2,6],[1,5,10],[4,2,9],[3,8,3]],2,2,3))