import sys

def f(n,k) :  # n 숫자를 k진수로 만들기, 
    result =[]
    notation = abs(k)
    if n==0 : return 0
    while  not (0<= n < notation) :
        if n%k == 0 or k > 0 :  t = n//k
        else :         t = n//k+1
        result.append(str(n-(k*t)))
        n = t
        # print(result,n,t,k)
    if  n!=0 : result.append(str(n))
    result.reverse()
    return ''.join(result)

num = int(sys.stdin.readline().rstrip())
print(f(num,-2))

# print(f(13,2))
# print(f(13,-2))
# print(f(-13,-2))
# print(f(13,-8))
# print(f(-13,-8))