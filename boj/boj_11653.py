import sys

def  dividable_primes(n, primes) :
    for _,e in enumerate(primes) : 
        if n%e==0 :
            return e
    return n

n   = int(sys.stdin.readline().rstrip())

# 에라토스테네스의 체(소수구하기)
primeset = [True]*n
for i  in range(2,int(n**0.5)+1) :
    if  primeset[i] == True :
        for j in range(i*2,n,i) :
            primeset[j] = False

primes = [ i for i,e in enumerate(primeset) if e and i not in [0,1]]  #n보다 적은 소수들만 모으기
while n !=1 :
    divider  = dividable_primes(n,primes)
    print(divider)
    n //= divider