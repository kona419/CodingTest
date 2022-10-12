def solution(array, commands):
    answer = []
    for com in commands:
        i = com[0]
        j = com[1]
        k = com[2]
        
        cut = array[i-1:j]
        cut.sort()
        answer.append(cut[k-1])
       
    return answer
