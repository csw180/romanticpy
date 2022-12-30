import sys
import itertools

def  gcd(a,b) :  # 최대공약수 유클리드호제법
    if  a%b == 0 :
        return b
    else :
        return gcd(b,a%b)

case  = int(sys.stdin.readline().rstrip())
cmdlist = []
for c in range(case) :
    cmdlist.append(sys.stdin.readline().rstrip())

for c in range(case)  :
    nums = list(map(int,cmdlist[c].split(" ")))[1:]
    ans = 0
    for a, b in itertools.combinations(nums, 2):
        ans += gcd(a, b)

    print(ans)