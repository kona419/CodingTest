# 내 풀이. 역시나 테케만 고려한 답이다.

def solution(citations):
    answer = 0
    count = 0
    for cit in citations:
        target = cit
        for c in citations:
            if target <= c:
                count += 1
        if count == target and len(citations) - count <= target:
            return target
          
# solution 1
def solution(citations):
    citations.sort(reverse=True)
    for idx , citation in enumerate(citations):
        if idx >= citation:
            return idx
    return len(citations)  # 마지막에 왜 길이를 리턴 하는걸까?
  
# solution 2

def solution(citations):
    citations.sort(reverse=True)
    answer = max(map(min, enumerate(citations, start=1)))
    return answer
  
  #1) min(index,value) 부분은 가능할 수 있는 모든 h-index를 추출하는 부분 
  #2) max(~) 값은 가능할 수 있는 모든 h-index 중 가장 큰 값을 추출하는 부분으로 생각하시면 됩니다. 
  #예를들어 [6, 5, 4, 1, 0]의 경우에선 min~ 부분은 min(1, 6), min(2, 5), min(3, 4), min(4, 1), min(5, 0), 
  #즉 해당 인용수 이상의 논문개수와 해당 논문의 인용수 중 더 작은 숫자를 고르는 작업을 하고(h-index로 가능한 숫자 추출), 
  #max~부분은 앞에서 골라진 (1, 2, 3, 1, 0) 중 가장 큰 숫자를 뽑아 실제 h-index를 구하는 방법입니다.
