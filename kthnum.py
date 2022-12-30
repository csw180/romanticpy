# 프로그래머스>k번째수 
def solution(arr, commands) :
  result = []
  for  comm in commands :
    l,m,k = comm
    b = a[l-1:m]
    b.sort()
    result.append(b[k-1])

  return result

a = [1, 5, 2, 6, 3, 7, 4]   
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
print(solution(a,commands))