def solution(numbers):
    result = []
    for  number in numbers :
        b = bin(number)[2:]
        p = b.rfind('0')  # 2진수로 표현했을때 마지막 0의 위치를 구한다
        prev = b[:p] if p!=-1 else '' #0의 위치앞쪽의 이진수
        mid = '10' if p!=len(b)-1 else ''  #0위치에서 '01 => '10' 으로 치환
        post = b[p+2:] if mid!='' else b[p:len(b)-2] + '1' #0의 위치 뒤쪽 이진수
        nextb = int(prev+mid+post,2)
        result.append(nextb)

    return result

numbers1 = [2,7]
print(f'solution={solution(numbers1)}')