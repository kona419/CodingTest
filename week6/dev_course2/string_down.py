def solution(s):
    answer = []
    result = ''
    for i in s:
        answer.append(i)
    answer.sort(reverse=True)
    for a in answer:
        result = result + a
    return result
