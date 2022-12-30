"""
백준 온라인저지 (boj.kr)
1918 후위표기식
중위 표기식이 주어졌을 때 후위 표기식으로 고치는 프로그램을 작성하시오
"""
import sys

expr  = sys.stdin.readline().rstrip()

stack = []
answer = []
for i,v in enumerate(expr) :
    if  v in ['+','-','*','/'] :
        if v in ['*','/'] :
           while stack and stack[-1] in ['*','/'] : answer.append(stack.pop())
        if  v in ['+','-'] :
           while stack and stack[-1] in ['+','-','*','/'] : answer.append(stack.pop())
        stack.append(v)
    elif v in ['(',')'] :
        if  v == '(' : stack.append(v)
        if  v == ')'  :
            while stack and stack[-1] != '(' :
                answer.append(stack.pop())
            stack.pop()
    else :
        answer.append(v)
while stack :  answer.append(stack.pop())
print(''.join(answer))