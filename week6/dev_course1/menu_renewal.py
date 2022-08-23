from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    
    for c in course:
        temp = []
        for order in orders:
            combi = combinations(sorted(order),c)
            temp += combi
        counter = Counter(temp)
        if len(counter)!=0 and max(counter.values()) != 1:
            for key, value in counter.items():
                if value == max(counter.values()):
                    answer.append("".join(key))
            
    
    return sorted(answer)
  
  # combinations와 counter를 사용하는 문제였다.
