# solution1
def solution(strings, n):
    strings.sort()
    answer = sorted(strings, key=lambda x : x[n])
    
    return answer
  
  # solution2
  def solution(strings, n):
    answer = sorted(strings, key=lambda x : (x[n],x))
    
    return answer
