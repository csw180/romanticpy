"""
백준 온라인저지 (boj.kr)
1935 후위표기식2
후위 표기식과 각 피연산자에 대응하는 값들이 주어져 있을 때, 그 식을 계산하는 프로그램을 작성하시오.
"""
import sys

case  = int(sys.stdin.readline().rstrip())
expr  = sys.stdin.readline().rstrip()
opnlist = []
for c in range(case) :
    opnlist.append(int(sys.stdin.readline().rstrip()))

opn_stack = []
for i,v in enumerate(list(expr)) :
    if  v in ['+','-','*','/'] : 
        op2 = opn_stack.pop()
        op1 = opn_stack.pop()
        if  v == '+' : opn_stack.append(op1+op2)
        elif  v == '-' : opn_stack.append(op1-op2)
        elif  v == '*' : opn_stack.append(op1*op2)
        else : opn_stack.append(op1/op2)
    else :
        opn_stack.append(opnlist[ord(v)-65])
print('{:.2f}'.format(opn_stack[0]))
