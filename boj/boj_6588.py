"""
백준 온라인저지 (boj.kr)
6588 골드바흐의 추측
1742년, 독일의 아마추어 수학가 크리스티안 골드바흐는 레온하르트 오일러에게 다음과 같은 추측을 제안하는 편지를 보냈다.
4보다 큰 모든 짝수는 두 홀수 소수의 합으로 나타낼 수 있다.
예를 들어 8은 3 + 5로 나타낼 수 있고, 3과 5는 모두 홀수인 소수이다. 
또, 20 = 3 + 17 = 7 + 13, 42 = 5 + 37 = 11 + 31 = 13 + 29 = 19 + 23 이다.
이 추측은 아직도 해결되지 않은 문제이다.
백만 이하의 모든 짝수에 대해서, 이 추측을 검증하는 프로그램을 작성하시오.
"""

import sys

def isodd(n) :
    if n%2==1 : return True
    else : return False

def isprime(n:int)-> bool :
    sqrt_value = n**(1/2) #n 까지 다 나눠볼필요없이 루트n 까지만 나눠보면된다. 루트n보다 큰수에는 소수가 발생하지 않는다.
    if n==1 : return False
    for i  in range(2,int(sqrt_value)+1) :
        if n%i == 0 : return False
    return True

nums = []
while True :
    num  =int(sys.stdin.readline().rstrip())
    if  num == 0 : break
    nums.append(num)


for _,v in enumerate(nums) :
    for i in range(1,(v//2)+1,2) :
        if  isodd(v-i) and isprime(i) and isprime(v-i):
            print('{} = {} + {}'.format(v,i,v-i))
            break

