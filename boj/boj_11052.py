import sys

n  =int(sys.stdin.readline().rstrip())
pi = list(map(int,sys.stdin.readline().rstrip().split(" ")))
if n==1 : print(pi[0])
else : 
    for i in range(1,n) :
        max_v = []
        for j in range(0,(i//2)+1) :
            max_v.append(pi[j]+pi[i-j-1])
        pi[i] = max(pi[i],max(max_v))
    print(pi[-1])