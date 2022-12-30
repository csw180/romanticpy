# 프로그래머스 영어끝말잊기
def solution(n, words):
    flow = []
    for word in words :
        if flow and ( (flow[-1][-1]!=word[0]) or (flow.count(word) > 0)) :
            flow.append('Q')
            break
        else :
            flow.append(word)

    try :
        idx = flow.index('Q')
        mok = idx // n
        return idx+1-(mok*n),mok+1
    except ValueError :
        return 0,0

words1 = ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]
n1 = 3
print(f'p1 solution = {solution(n1,words1)}')

words2 = 	["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]
n2 = 3
print(f'p2 solution = {solution(n2,words2)}')

words3 = 	["hello", "one", "even", "never", "now", "world", "draw"]
n3 = 2
print(f'p3 solution = {solution(n3,words3)}')