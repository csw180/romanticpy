"""
백준 온라인저지 (boj.kr)
10808 알파벳 개수
알파벳 소문자로만 이루어진 단어 S가 주어진다. 각 알파벳이 단어에 몇 개가 포함되어 있는지 구하는 프로그램을 작성하시오
"""
import sys
from typing import Counter

expr  = sys.stdin.readline().rstrip()
c = Counter(expr)
answer = []
for  a in range(97,123) :
    answer.append(c.get(chr(a),0))

print(*answer)