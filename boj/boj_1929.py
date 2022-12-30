"""
백준 온라인저지 (boj.kr)
1929 소수구하기
M이상 N이하의 소수를 모두 출력하는 프로그램을 작성하시오.
"""
import sys
import math

def isprime(n:int)-> bool :
    sqrt_value = n**(1/2) #n 까지 다 나눠볼필요없이 루트n 까지만 나눠보면된다. 루트n보다 큰수에는 소수가 발생하지 않는다.
    if n==1 : return False
    for i  in range(2,math.floor(sqrt_value)+1) :
        if n%i == 0 : return False
    return True

nums  = list(map(int,sys.stdin.readline().rstrip().split(' ')))

answer = []
for i in range(nums[0], nums[1]+1) :
    if isprime(i) : print(i)