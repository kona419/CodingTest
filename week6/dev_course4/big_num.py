# 내가 생각한 풀이. 뒤에서 부터 잘라서 가장 큰 값을 pop해서 넣기.

def solution(number, k):
    answer = ''
    number = list(map(int, number))
    length = len(number)
    
    for i in range(length-k-1, 0,-1):
        num = sorted(number[:-i])     # num에서 큰 값을 pop 해도 numbers는 변화X
        answer += "".join(str(num.pop()))
    
    return answer
  
# solution
def solution(number, k):
    answer = [] # Stack
    
    for num in number:
        if not answer:
            answer.append(num)
            continue
        if k > 0:
            while answer[-1] < num:
                answer.pop()
                k -= 1
                if not answer or k <= 0:
                    break
        answer.append(num)
        
    answer = answer[:-k] if k > 0 else answer
    return ''.join(answer)
