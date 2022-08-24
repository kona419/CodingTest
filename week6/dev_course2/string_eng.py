def solution(s):
    eng = {'zero': '0', 'one':'1', 'two':'2', 'three':'3', 'four':'4', 'five':'5', 'six':'6', 'seven':'7','eight':'8', 'nine':'9'}
    
    for key in eng:
        s = s.replace(key, eng[key])        # key : 기존 문자열에서 key와 같은 부분을 replace
        
    return int(s)
    
    # 딕셔너리 타임 사용 - { ' ' : ' '}
    # replace 사용 - replace(old, new, [count])
