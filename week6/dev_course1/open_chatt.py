def solution(record):
    answer = []
    actions = []
    userDB = dict()
    
    for event in record:
        info = event.split()
        action = info[0]
        uid = info[1]
        if action in ("Enter", "Change"):
            nick = info[2]
            userDB[uid] = nick
        actions.append((action,uid))
        
    for acionInfo in actions:
        action = acionInfo[0]
        uid = acionInfo[1]
        if action == "Enter":
            answer.append(f'{userDB[uid]}님이 들어왔습니다.')
        elif action == "Leave":
            answer.append(f'{userDB[uid]}님이 나갔습니다.')
    
    return answer
  
  # 닉네임이 바뀌는 것을 구현하기 위해 딕셔너리를 사용한다. 딕셔너리를 사용하는 것이 핵심이였다.
  
