"""
백준 온라인저지 (boj.kr)
10828 스택
정수를 저장하는 스택을 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.

명령은 총 다섯 가지이다.

push X: 정수 X를 스택에 넣는 연산이다.
pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
size: 스택에 들어있는 정수의 개수를 출력한다.
empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
"""
# case = 14
# cmdlist = []
# cmdlist.append('push 1')
# cmdlist.append('push 2')
# cmdlist.append('top')
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
# cmdlist.append('top')

# case = 7
# cmdlist = []
# cmdlist.append('pop')
# cmdlist.append('top')
# cmdlist.append('push 123')
# cmdlist.append('top')
# cmdlist.append('pop')
# cmdlist.append('top')
# cmdlist.append('pop')
# cmdlist.append('pop')

case =  int(input())
cmdlist = []
for i in range(case) :
    cmdlist.append(input())

stack = []

for caseid in range(case) :
    cmd = cmdlist[caseid].split(' ')
    if  cmd[0] == 'push' :
        stack.append(int(cmd[1]))
        continue
    if  cmd[0] == 'pop' :
        try : 
            n = stack.pop(-1)
        except  IndexError  :
            print(-1)
        else :
            print(n)
        continue    
    if  cmd[0] == 'top' :
        try :
            n =  stack[-1]
        except  IndexError  :
            print(-1)
        else : 
            print(n)
        continue
    if  cmd[0] == 'size' :
        print(len(stack))
        continue
    if  cmd[0] == 'empty' :
        if  len(stack) == 0 :
            print(1)
        else :
            print(0)
    


        

