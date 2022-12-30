import sys

def f(n)  :
    if n==1 : return 1
    if n==2 : return 2
    if n==3 : return 4
    else :
        return f(n-1) + f(n-2) + f(n-3)

n  = int(sys.stdin.readline().rstrip())
cases = []
for i in range(n) :
    cases.append(int(sys.stdin.readline().rstrip()))

for _,v in enumerate(cases) :
    print(f(v))
