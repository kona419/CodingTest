from collections import deque
def solution(queue1, queue2):
    
    total = sum(queue1)+sum(queue2)
    if total %2 != 0:
        return -1
    count = 0
    goal = total // 2
    
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    sum_1 = sum(queue1)
    sum_2 = sum(queue2)
                
    while count <= 6000000:
        if sum_1 == sum_2:
            return count
        if sum_1 > sum_2:
            q1 = queue1.popleft()
            queue2.append(q1)
            sum_1 -= q1
            sum_2 += q1    
            count+=1
        else:
            q2 = queue2.popleft()
            queue1.append(q2)
            sum_2 -= q2
            sum_1 += q2
            count+=1
    return -1

  # sum 을 while문 안에 넣었더니 시간초과가 떴다.
  # while 조건을 True로 하니 시간 초과가 떴다
  # 큐를 구현할 때는 무조건 from collections import deque를 쓰자!
