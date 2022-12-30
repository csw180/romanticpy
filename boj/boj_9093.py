
"""
백준 온라인저지 (boj.kr)
9093 단어뒤집기
문장이 주어졌을 때, 단어를 모두 뒤집어서 출력하는 프로그램을 작성하시오. 
단, 단어의 순서는 바꿀 수 없다. 단어는 영어 알파벳으로만 이루어져 있다.
"""
# case = 2
# cmdlist = []
# cmdlist.append('I am happy today')
# cmdlist.append('We want to win the first prize')

case =  int(input())
cmdlist = []
for i in range(case) :
    cmdlist.append(input())

for caseid in range(case) :
    tokens = cmdlist[caseid].split(' ')
    rvs_token = []
    for _,e in enumerate(tokens) :
        rvs_token.append(e[::-1])
    print(' '.join(rvs_token))
