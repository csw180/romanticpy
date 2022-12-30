"""
백준 온라인저지 (boj.kr)
10845 큐
정수를 저장하는 큐를 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.

명령은 총 여섯 가지이다.

push X: 정수 X를 큐에 넣는 연산이다.
pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
size: 큐에 들어있는 정수의 개수를 출력한다.
empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
"""

# case = 15
# cmdlist = []

# cmdlist.append('push 1')
# cmdlist.append('push 2')
# cmdlist.append('front')
# cmdlist.append('back')
# cmdlist.append('size')
# cmdlist.append('empty')
# cmdlist.append('pop')
# cmdlist.append('pop')
# cmdlist.append('pop')
# cmdlist.append('size')
# cmdlist.append('empty')
# cmdlist.append('pop')
# cmdlist.append('push 3')
# cmdlist.append('empty')
# cmdlist.append('front')

from collections import deque
import sys

case  = int(sys.stdin.readline().rstrip())
cmdlist = []
for c in range(case) :
    cmdlist.append(sys.stdin.readline().rstrip())

d = deque()
for idx,acmd in enumerate(cmdlist) :
    cmd = acmd.split(' ');
    if  cmd[0] == 'push' :
        d.append(int(cmd[1]))
    elif  cmd[0] == 'pop' :
        if  d : print(d.popleft())
        else :  print(-1)
    elif  cmd[0] == 'front' :
        if  d : print(d[0])
        else :  print(-1)
    elif  cmd[0] ==  'back' :
        if  d : print(d[-1])
        else : print(-1)
    elif  cmd[0] ==  'size' :
        print(len(d))
    elif  cmd[0] == 'empty' :
        if  len(d) == 0 : print(1)
        else : print(0)