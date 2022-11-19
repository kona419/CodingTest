# 1st answer : time out
def solution(number, limit, power):
    answer = 0
    divs = []
    count = 0
    for i in range(1, number+1):
        count = 0
        for j in range(1, i+1):
            if i%j == 0:
                count += 1
        divs.append(count)
    for div in divs:
        if div <= limit:
            answer += div
        else:
            answer += power
    return answer
  
# 2nd answer : pass  
def solution(number, limit, power):
    answer = 0
    divs = []
    count = 0
    for i in range(1, number+1):
        count = 0
        for j in range(1, int(i**(1/2))+1):
            if i%j == 0:
                count += 1
                if ((j**2) != i) :
                    count +=1
        divs.append(count)
    for div in divs:
        if div <= limit:
            answer += div
        else:
            answer += power
    return answer
