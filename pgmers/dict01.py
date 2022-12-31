# 프로그래머스 > 코딩테스트 연습 > 위클리 챌린지 > 모음사전

from itertools import product

def solution(word) :
  chars = ['A', 'E', 'I', 'O', 'U']

  diclist = []
  for i  in range(1,len(chars)+1) :
    p  = [''.join(e) for e in  product(chars,repeat=i)]
    diclist.extend(p)

  diclist.sort()
  return diclist.index(word)+1

word1 = "AAAAE"
print(f'{word1} solution= {solution(word1)}')

word2 = "AAAE"
print(f'{word2} solution= {solution(word2)}')

word3 = "I"
print(f'{word3} solution= {solution(word3)}')

word4 = "EIO"
print(f'{word4} solution= {solution(word4)}')
