"""
백준 온라인저지 (boj.kr)
1406 에디터
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
0.3 초 (하단 참고)	512 MB	54934	15222	10042	26.882%
문제
한 줄로 된 간단한 에디터를 구현하려고 한다. 
이 편집기는 영어 소문자만을 기록할 수 있는 편집기로, 최대 600,000글자까지 입력할 수 있다.

이 편집기에는 '커서'라는 것이 있는데, 커서는 문장의 맨 앞(첫 번째 문자의 왼쪽), 
문장의 맨 뒤(마지막 문자의 오른쪽), 또는 문장 중간 임의의 곳(모든 연속된 두 문자 사이)에 위치할 수 있다. 
즉 길이가 L인 문자열이 현재 편집기에 입력되어 있으면, 커서가 위치할 수 있는 곳은 L+1가지 경우가 있다.
"""
# text = 'abc'
# case = 9
# cmdlist = []
# cmdlist.append('L')
# cmdlist.append('L')
# cmdlist.append('L')
# cmdlist.append('L')
# cmdlist.append('L')
# cmdlist.append('P x')
# cmdlist.append('L')
# cmdlist.append('B')
# cmdlist.append('P y')

import sys

text = sys.stdin.readline().rstrip()
case = int(sys.stdin.readline().rstrip())
cmdlist = []
for c in range(case) :
    cmdlist.append(sys.stdin.readline().rstrip())

lstack = list(text)
rstack = []

for _, cmdstr  in  enumerate(cmdlist) :
    cmds =  cmdstr.split(' ')
    if  cmds[0] == 'L' :
        if lstack :
            rstack.append(lstack.pop())
        continue
    elif  cmds[0] == 'P' :
        lstack.append(cmds[1])
        continue
    elif  cmds[0] == 'B' :
        if lstack :
            lstack.pop()
        continue
    elif  cmds[0] == 'D' :
        if rstack :
            lstack.append(rstack.pop())

lstack.extend(rstack[::-1])
print(''.join(lstack))