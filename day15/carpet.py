# solution1 : i가 yellow의 약수일때, x=몫, y=i이고 이때 yellow_x*2+yellow_y*2 +4 ==brown 이면 x와 y에 +2해서 append 후 리턴.

def solution(brown, yellow):
    answer = []
    
    yellow_x = 0
    yellow_y = 0
    
    for i in range(1, yellow+1):
        if yellow % i ==0:
            yellow_x = int(yellow/i)
            yellow_y = i
            if yellow_x*2+yellow_y*2 +4 ==brown:
                answer.append(yellow_x+2)
                answer.append(yellow_y+2)
                return sorted(answer, reverse = True)

    return answer

  
# solution2 : i가 yellow의 약수일때, x=몫, y=i이고 각각 +2 해줌. 이때, x*y == brown+yellow 이면 append 후 리턴.

def solution(brown, yellow):
    answer = []
    x = 0
    y = 0
    
    for i in range(1, yellow+1):
        if yellow%i == 0:
            x = yellow//i + 2
            y = i + 2
            if x*y == brown+yellow:
                answer.append(x)
                answer.append(y)
                return answer
