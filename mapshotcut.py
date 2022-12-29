# 프로그래머스 연습문제 > 게임맵최단거리
# https://school.programmers.co.kr/learn/courses/30/lessons/1844

from collections import deque

def solution(maps):
    _MAXROWIDX = len(maps)-1
    _MAXCOLIDX = len(maps[0])-1
    
    queue = deque()
    queue.append((0,0,1))
    while queue :
        r,c,n = queue.popleft()
        maps[r][c] = 0
        if r==_MAXROWIDX and c==_MAXCOLIDX :
            return n
        if c < _MAXCOLIDX and maps[r][c+1]==1 :
            queue.append((r,c+1,n+1))
        if c > 0 and maps[r][c-1]==1 :
            queue.append((r,c-1,n+1))
        if r < _MAXROWIDX and maps[r+1][c]==1 :
            queue.append((r+1,c,n+1))
        if r > 0 and maps[r-1][c]==1 :
            queue.append((r-1,c,n+1))
        # print(r,c,queue)
    return -1

# def solution(maps):
#     maps=[[0]*(len(maps[0])+1)]+[[0,*maps[i]] for i in range(len(maps))]
#     _MAXROWIDX = len(maps)-1
#     _MAXCOLIDX = len(maps[0])-1

#     queue = deque()
#     queue.append((1,1,1))
#     while queue :
#         r,c,n = queue.popleft()
#         maps[r][c] = 0
#         if r==_MAXROWIDX and c==_MAXCOLIDX :
#             return n
#         if c < _MAXCOLIDX and maps[r][c+1]==1 :
#             queue.append((r,c+1,n+1))
#         if c > 1 and maps[r][c-1]==1 :
#             queue.append((r,c-1,n+1))
#         if r < _MAXROWIDX and maps[r+1][c]==1 :
#             queue.append((r+1,c,n+1))
#         if r > 1 and maps[r-1][c]==1 :
#             queue.append((r-1,c,n+1))
#         # print(r,c,queue)
#     return -1

print(f'answer={solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]])}')