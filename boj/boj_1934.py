"""
백준 온라인저지 (boj.kr)
1934 최소공배수
두 자연수 A와 B에 대해서, A의 배수이면서 B의 배수인 자연수를 A와 B의 공배수라고 한다. 
이런 공배수 중에서 가장 작은 수를 최소공배수라고 한다. 예를 들어, 6과 15의 공배수는 30, 60, 90등이 있으며, 
최소 공배수는 30이다.
두 자연수 A와 B가 주어졌을 때, A와 B의 최소공배수를 구하는 프로그램을 작성하시오.
"""
import sys

def  gcd(a,b) :  # 최대공약수 유클리드호제법
    if  a%b == 0 :
        return b
    else :
        return gcd(b,a%b)

case = int(sys.stdin.readline().rstrip())
intexts = []
for c in range(case) :
    intext  = sys.stdin.readline().rstrip()
    intexts.append(intext)

for i,v in enumerate(intexts) :
    nums = list(map(int,v.split(' ')))
    print( (nums[0] *nums[1]) // gcd(nums[0], nums[1])) # 두수의 곱을 최대공약수로 나누면 최소공배수