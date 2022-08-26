# 내 답 : 랜덤이여서 맞을 때가 있고 아닐때가 있다...
import random
import math

def solution(numbers):
    answer = ''
    result = []
    time = math.factorial(len(numbers))
    for i in range(time):
        random.shuffle(numbers)
        for num in numbers:
            answer += str(num)
        if int(answer) in result:
            time -= 1
        else:
            result.append(int(answer))
        answer = ''
    
    return str(max(result))
  
# solution

def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*3, reverse=True)
    return str(int(''.join(numbers)))
  
  # 문자열 비교는 ASCII 값으로 치환되어 정렬된다. 따라서 666, 101010, 222의 첫번째 인덱스 값으로 비교한다. 첫번째 값인 6, 1, 2 비교.
  # 그래서 x*3을 해준다
  # 마지막에 str int는 '0000' 같은 걸 '0'으로 바꾸기 위해서 작성
  # 이 문제는 결국 주어진 숫자 중에서 앞자리가 제일 큰게 앞에 와야 한다.
  
  # 이걸 어케 하노...ㅅㅂ
  # 문제를 너무 곧이 곧대로 받아들여서 푸는 것 같다.. 그 속에 있는 진짜를 
