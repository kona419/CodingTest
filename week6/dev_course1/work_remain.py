import math

def solution(progresses, speeds):
    days = []
    answer = []
    index = 0
    
    for i in range(len(progresses)):
        remain = 100 - progresses[i]
        day = math.ceil(remain / speeds[i])
        days.append(day)
        
    for i in range(len(days)):
        if days[index] < days[i]:
            answer.append(i-index)
            index = i
    answer.append(len(days) - index)

    return answer
  
  # 지금보다 큰 숫자가 나오면 거기까지 인덱스 계산. 지금을 인덱스로 치환.
  # ~~ 반복하면 마지막에는 제일 작은 애들만 남으면 전체 길이에서 인덱스 
