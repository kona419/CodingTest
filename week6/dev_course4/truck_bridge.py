# 내답 - 테케 통과, 히든케 실패
def solution(bridge_length, weight, truck_weights):
    answer = 0
    summ = 0
    b_length = int(bridge_length)
    weight = int(weight)
    t_length = len(truck_weights)
    
    if t_length > b_length :
        for i in range(t_length):
            for j in range(b_length):
                summ += truck_weights[j]
            if summ <= 10:
                answer += b_length+1
                j+=1
            else:
                answer += b_length
    
        
    else:
        if sum(truck_weights) <= weight:
            answer += b_length
            answer += len(truck_weights)
        
    return answer
  
  # 통과한 답
  
  def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = [0 for _ in range(bridge_length)]
    
    while bridge:
        answer+=1
        bridge.pop(0)
        
        if truck_weights:
            if sum(bridge) + truck_weights[0] <= weight:
                t = truck_weights.pop(0)
                bridge.append(t)
            else:
                bridge.append(0)
        
    return answer
