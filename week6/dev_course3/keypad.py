
def solution(numbers, hand):
    answer = ''
    
    dic = {1: [0, 0], 2: [0, 1], 3: [0, 2],
           4: [1, 0], 5: [1, 1], 6: [1, 2],
           7: [2, 0], 8: [2, 1], 9: [2, 2],
           '*':[3, 0], 0: [3, 1], '#': [3, 2]}
    
    left_s = dic['*']
    right_s = dic['#']
    
    for num in numbers:
        now = dic[num]
        if num in [1,4,7]:
            answer += 'L'
            left_s = now
            
        elif num in [3,6,9]:
            answer += 'R'
            right_s = now
            
        else:
            left_d, right_d = 0, 0
            for a,b,c in zip(left_s, right_s, now):
                left_d += abs(a-c)
                right_d += abs(b-c)
                
            if left_d < right_d:
                answer += 'L'
                left_s = now
            elif left_d > right_d:
                answer += 'R'
                right_s = now
            else:
                if hand == 'right':
                    answer += 'R'
                    right_s = now
                else:
                    answer += 'L'
                    left_s = now
            
    return answer
  
  # 처음에 BFS가 떠올라서 BFS로 구현했다.
  # 그러나 기존 BFS와 다른 것을 매번 시작점이 바뀐다는 것. 
  # 키패드가 12개 밖에 없기 때문에 딕셔너리로 하는게 더 간단하다.
