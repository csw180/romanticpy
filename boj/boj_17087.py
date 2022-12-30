import sys

def  gcd(a,b) :  # 최대공약수 유클리드호제법
    if  a%b == 0 :
        return b
    else :
        return gcd(b,a%b)


n,s  = list(map(int,sys.stdin.readline().rstrip().split(" ")))
nums = list(map(int,sys.stdin.readline().rstrip().split(" ")))

a = [abs(s-nums[i]) for i in range(n)]
g = min(a)
for _,v in enumerate(a) :
    g = gcd(v,g)

print(g)