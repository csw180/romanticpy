"""
백준 온라인저지 (boj.kr)
2609 최대공약수와 최소공배수
두 개의 자연수를 입력받아 최대 공약수와 최소 공배수를 출력하는 프로그램을 작성하시오.
"""
import sys

def  gcd(a,b) :  # 최대공약수 유클리드호제법
    if  a%b == 0 :
        return b
    else :
        return gcd(b,a%b)

nums  = list(map(int,sys.stdin.readline().rstrip().split(' ')))
print(gcd(nums[0], nums[1]))
print( (nums[0] *nums[1]) // gcd(nums[0], nums[1])) # 두수의 곱을 최대공약수로 나누면 최소공배수