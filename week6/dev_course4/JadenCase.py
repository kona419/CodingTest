# 내 답 - 테케 통과, 히든케이스 실패

def solution(s):
    answer = ''
    s = s.split()
    for i in s:
        if (i[0]).isdigit():
            answer += i[0]
            answer += (i[1:]).lower()
            answer += ' '
        else:
            answer += (i[0]).upper()
            answer += (i[1:]).lower()
            answer += ' '
    return answer[:-1]
  
  # 공백이 2개 있으면 2개가 그대로 나와야 함.
  
  def solution(s):
    answer = ''
    
    words = s.split(' ')

    for i in range(len(words)):
        words[i] = words[i].capitalize()
        
    answer = ' '.join(words)
    
    return answer
  
  # capitalize() : 자동으로 처음은 대문자, 그 뒤는 소문자. 첫문자가 숫자면 무시하고 뒤에는 소문자.
  # s.split(' ') : 이거로 해야 공백 2개면 2개 그대로 받아옴. ' ' 없으면 공백2개가 1개가 되버림.
