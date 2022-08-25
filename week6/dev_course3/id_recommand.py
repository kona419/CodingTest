def solution(new_id):
    answer = ''
    new_id = new_id.lower()
    
    oper = ['-','_','.']
    
    for i in new_id:
        if i.isalpha():
            answer += i
        elif i.isdigit():
            answer += i
        elif i in oper:
            answer += i
            
    while '..' in answer:
        answer = answer.replace("..", ".")
        
    if answer[0] == '.' :
        if len(answer) > 1:
            answer = answer[1:]
        else:                              #4에서 if문을 또 쓰는 이유 : 
            answer = '.'                   #4에서 문자열이 '.'인 경우 즉, len(answer) = 1인 경우 슬라이싱에서 오류가 발생하기 때문입니다! 
                                           #뒷 코드에서 마지막에 오는 '.'을 제거할 때 제거하겠다는거죠
            
    if answer[-1] == '.' :
        answer = answer[:-1]
        
    if answer == '':
        answer = 'a'
        
    elif len(answer) > 15:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]
        
    while len(answer) <3 :
        answer += answer[-1]
    
    return answer
