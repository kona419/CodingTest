# 내 답 - deque를 활용해 큐를 사용해야 한다고 생각했다.

from collections import deque
priorities = [1, 1, 9, 1, 1, 1]
queue = deque(priorities)

for pri in priorities:
    now = queue.popleft()
    right = queue.popleft()
        
    if right > now:
        queue.append(now)
        queue.appendleft(right)
    else:
        queue.appendleft(right)
        queue.appendleft(now)
            
print(queue)

# 결국 큰 수 먼저 출력하는 것.
# 숫자가 같다면 앞에서 부터 출력.

def solution(priorities, location):
    answer = 0
    while True:
        max_num = max(priorities)
        for i in range(len(priorities)):
            if max_num == priorities[i]:
                answer+=1
                priorities[i] = 0
                max_num = max(priorities)
                if i == location:
                    return answer
