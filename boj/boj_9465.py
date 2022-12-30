import sys

def crdscor(n,cardrow,cards) :  #card score 리턴
    if n<0 : return 0
    else :
        return cards[cardrow][n]

case  = int(sys.stdin.readline().rstrip())
probs = []
for  c in range(case) :
    prob = []
    prob.append(int(sys.stdin.readline().rstrip()))
    prob.append(list(map(int,sys.stdin.readline().rstrip().split(" "))))
    prob.append(list(map(int,sys.stdin.readline().rstrip().split(" "))))
    probs.append(prob)

for  i,v  in enumerate(probs) :
    n = v[0]
    cards = [v[1],v[2]]
    for j  in range(n) :
        cards[0][j] = max(crdscor(j-1,1,cards),crdscor(j-2,1,cards))+cards[0][j]
        cards[1][j] = max(crdscor(j-1,0,cards),crdscor(j-2,0,cards))+cards[1][j]
    print(max(cards[0][-1],cards[1][-1]))