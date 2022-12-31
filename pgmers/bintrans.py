
# 프로그래머스 > 코딩테스트 연습>월간 코드 챌린지 시즌1>이진 변환 반복하기

def  trans(s) :
  cnt = s.count('0')
  s = s.replace('0','')
  return cnt,bin(len(s))[2:]


def solution(s) :

  zcnt =0
  loop = 0

  while s != '1' :
    c, s= trans(s)
    zcnt +=c
    loop+=1

  return [loop,zcnt]

s1 = "110010101001"
print(f's1 solution={solution(s1)}')

s2 = "01110"
print(f's2 solution={solution(s2)}')

s3 = "1111111"
print(f's3 solution={solution(s3)}')
