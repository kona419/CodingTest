# 반복문 써서 구현
def solution(arr):
    answer = 0
    n = 1
    
    while True:
        answer = max(arr)*n
        result = True
        for a in arr:
            if answer %a != 0:
                result = False
                break
        if result:
            break
        n += 1
    return answer
  
# gcd : 최대공약수 구하는 함수 사용
from fractions import gcd

def solution(num):      
    answer = num[0]
    for n in num:
        answer = n * answer / gcd(n, answer)

    return answer
