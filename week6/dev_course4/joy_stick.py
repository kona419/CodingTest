# A를 고려하지 않은 나의 코드

def solution(name):
    answer = [ord('A')]*len(name)
    count = 0
    
    name = list(name)
    
    for n in name:
        if ord(n) <= 78:
            count += ord(n) - ord('A')
        else:
            count += ord('Z') - ord(n) +1
    count += len(name)-1
       
    return count

  # 답
  def solution(name):

	# 조이스틱 조작 횟수 
    answer = 0
    
    # 기본 최소 좌우이동 횟수는 길이 - 1
    min_move = len(name) - 1
    
    for i, char in enumerate(name):
    	# 해당 알파벳 변경 최솟값 추가
        answer += min(ord(char) - ord('A'), ord('Z') - ord(char) + 1)  # 앞에서부터 가는거랑 뒤에서부터 가는 것 중에 짧은 것.
        
        # 해당 알파벳 다음부터 연속된 A 문자열 찾기
        next = i + 1
        while next < len(name) and name[next] == 'A':
            next += 1
            
        # 기존, 연속된 A의 왼쪽시작 방식, 연속된 A의 오른쪽시작 방식 비교 및 갱신
        min_move = min([min_move, 2 *i + len(name) - next, i + 2 * (len(name) -next)])
        
    # 알파벳 변경(상하이동) 횟수에 좌우이동 횟수 추가
    answer += min_move
    return answer
