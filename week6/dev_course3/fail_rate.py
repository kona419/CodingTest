# result는 dictionary이므로 #sorted에 result를 그냥 넘기면 result의 keys가 들어갑니다. keys는 생략이 가능합니다. 거기에 lambda는 기준을 result[x]: 즉 value로 정렬한다는 뜻입니다. 그래서 key가 출력되게 됩니다.

def solution(N, stages):
    answer = {}
    length = len(stages)
    
    for i in range(1, N+1):
        if i in stages:
            answer[i] = stages.count(i)/length
            length -= stages.count(i)
        else:
            answer[i] = 0
    result = sorted(answer.keys(), key = lambda x:answer[x], reverse=True)
    return result
        
    # 정렬할때 인덱스 값을 써야 한다면 딕셔너리를 떠올리자!!!!
