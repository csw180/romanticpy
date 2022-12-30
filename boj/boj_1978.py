"""
백준 온라인저지 (boj.kr)
1978 소수찾기
주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.
"""
import sys
import math

case  = int(sys.stdin.readline().rstrip())
nums  = list(map(int,sys.stdin.readline().rstrip().split(' ')))

def isprime(n:int)-> bool :
    sqrt_value = n**(1/2) #n 까지 다 나눠볼필요없이 루트n 까지만 나눠보면된다. 루트n보다 큰수에는 소수가 발생하지 않는다.
    if n==1 : return False
    for i  in range(2,math.floor(sqrt_value)+1) :
        if n%i == 0 : return False
    return True

answer = []
for _,v in enumerate(nums):
    if isprime(v) : answer.append(v)

print(len(answer))