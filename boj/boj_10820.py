"""
백준 온라인저지 (boj.kr)
10820 문자열 분석
문자열 N개가 주어진다. 이때, 문자열에 포함되어 있는 소문자, 대문자, 숫자, 공백의 개수를 구하는 프로그램을 작성하시오.
각 문자열은 알파벳 소문자, 대문자, 숫자, 공백으로만 이루어져 있다.
"""

while True :
    try :
        expr = input()

        low_cnt, upp_cnt, num_cnt, sp_cnt = 0,0,0,0
        for _,v in enumerate(expr) :
            if  v.islower() : low_cnt +=1
            if  v.isupper() : upp_cnt +=1
            if  v.isnumeric() : num_cnt +=1
            if  v.isspace() : sp_cnt +=1
        print(low_cnt, upp_cnt, num_cnt, sp_cnt)
    except EOFError :
        break