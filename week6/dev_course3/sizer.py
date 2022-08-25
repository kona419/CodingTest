def solution(s, n):
    s = list(s)
    
    for i in range(len(s)):
        if s[i].isupper():
            s[i]=chr((ord(s[i])-ord('A')+ n)%26+ord('A'))
        elif s[i].islower():
            s[i]=chr((ord(s[i])-ord('a')+ n)%26+ord('a'))

    return "".join(s)
  
  # 아스키코드로 해결해야 된다는 것을 캐치했다.
  # 리스트로 바꾸지 않고 string 그대로 계산 했는데 히든 케이스에서 다 실패했음... 테케는 다 성공했는데.....
