# my answer. 히든 케이스에서 막힘
def solution(n, lost, reserve):
    answer = 0
    answer = answer+(n-len(lost))
    
    for lo in lost:
        if lo in reserve:
            reserve.remove(lo)
            lost.remove(lo)
            answer+=1
    
    for lo in lost:
        if lo-1 in reserve:
            reserve.remove(lo-1)
            answer+=1
            continue
        if lo+1 in reserve:
            reserve.remove(lo+1)
            answer+=1
            continue
        
    
    return answer
  
  # answer
  def solution(n, lost, reserve):
    set_reserve = set(reserve) - set(lost)
    set_lost = set(lost) - set(reserve)
    
    for i in set_reserve:
        if i-1 in set_lost:
            set_lost.remove(i-1)
        elif i+1 in set_lost:
            set_lost.remove(i+1)
        
    
    return n-len(set_lost)
