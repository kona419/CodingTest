from itertools import combinations

def solution(numbers, target):
    answer = 0
    queue = [[numbers[0],0], [-1*numbers[0],0]]
    n = len(numbers)
    while queue:
        temp, idx = queue.pop()
        idx += 1
        if idx < n:
            queue.append([temp+numbers[idx], idx])
            queue.append([temp-numbers[idx], idx])
        else:
            if temp == target:
                answer+=1

    return answer
  
  # 트리 구조를 활용해 푸는 문제였다. DFS를 사용해서.
  # 원래 랜덤 조합을 이용해서 풀려고 했는데 불가능한 것 같다.
