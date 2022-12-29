# 프로그래머스 연습문제 > 문자열 나누기
# https://school.programmers.co.kr/learn/courses/30/lessons/140108

def split2(s) :
    delim = s[0]
    same = 0
    diff = 0
    matched = 0
    for i,v in enumerate(s):
        if v==delim :
            same+=1
        else :
            diff+=1
        if  same==diff :
            matched+=1
            if i+1==len(s) :
                return matched
            same, diff = 0,0
            delim = s[i+1]
            continue
    return matched+1

print(split2("banana"))
print(split2("abracadabra"))
print(split2("aaabbaccccabba"))
