def solution(s):
    answer = ''
    s = list(map(int, s.split(' ')))
    answer = str(min(s))+ ' '+str(max(s))
    return answer
  
  # str을 int로 어떻게 바꿀까해서 리스트도 만들고 했는데 map을 쓰면 된다.!
  # str -> int using map!!!
