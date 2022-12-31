# 프로그래머스 > 코딩테스트연습 > 탐욕법(greedy) > 구명보트

def solution(people, limit):
    people.sort()

    left, right = 0, len(people) - 1
    count = 0
    while left <= right:
        if people[left] + people[right] <= limit:
            count += 1
            left += 1
            right -= 1
        else:
            count += 1
            right -= 1
    return count

people = [70, 50, 80, 50]
limit  = 100
print(solution(people,limit))