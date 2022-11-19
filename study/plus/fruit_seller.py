def solution(k, m, score):
    answer = 0
    box_cnt = 0
    score.sort(reverse=True)
    news=[score[i:i + m] for i in range(0, len(score), m)]

    for new in news:
        len_new = len(new)
        if len_new == m:
            box_cnt+=1
            
    for new in news:
        min_new = min(new)
        len_new = len(new)
        if len_new == m:
            if min_new <= k:
                answer += (min_new*m)
            else:
                answer += (k*m)
    return answer
