"""
백준 온라인저지 (boj.kr)
11656 접미사배열
접미사 배열은 문자열 S의 모든 접미사를 사전순으로 정렬해 놓은 배열이다.
baekjoon의 접미사는 baekjoon, aekjoon, ekjoon, kjoon, joon, oon, on, n 으로 총 8가지가 있고, 
이를 사전순으로 정렬하면, aekjoon, baekjoon, ekjoon, joon, kjoon, n, on, oon이 된다.
문자열 S가 주어졌을 때, 모든 접미사를 사전순으로 정렬한 다음 출력하는 프로그램을 작성하시오.
"""
import sys
case  = sys.stdin.readline().rstrip()

answer = []
for i in range(len(case)) :
    answer.append(case[i:])

answer.sort()
for _,v in enumerate(answer) :
    print(v)
