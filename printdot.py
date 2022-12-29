
def solution(k, d):
    answer = 0
    # for i in range(0,d+1,k) :
    #     for j in range(0,d+1,k) :
    #         if ((i*i+j*j)**(1/2) > d) :
    #             break
    #         print(f'({i},{j})')
    #         answer+=1
    # d=7 k=2
    for i in range(0,d+1,k) :
        answer = answer + (d//k + 1) - i//k 
        print(i, (d//k + 1) - i//k )
    return answer

# print(solution(2,4))
print(solution(1,5))

# for 
# 0   d/2
# 1   d/2-1
# 2   d/2-2
# .
# .
# d    
