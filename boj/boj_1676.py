"""
백준 온라인저지 (boj.kr)
1676 팩토리얼 0의 개수
N!에서 뒤에서부터 처음 0이 아닌 숫자가 나올 때까지 0의 개수를 구하는 프로그램을 작성하시오.
"""
import sys

def nk(n,k) :
    count = 0
    i = 1
    while n >= k**i : 
        count += ( n // (k**i))
        i +=1
    return count

num  =int(sys.stdin.readline().rstrip())
print(min(nk(num,2),nk(num,5)))
