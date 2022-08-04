# solution1 : 힙큐 사용
import heapq

def solution(operations):
    answer = []
    heap = []   # 힙 생성

    for data in operations:
        # 연산이 "I"일 경우 공백 뒤의 숫자를 heap에 넣음
        if data[0] == "I":
            heapq.heappush(heap, int(data[2:]))
        # 연산이 "D"일 경우
        else:
            if len(heap) == 0:
                pass
            # 공백 뒤가 "-"일 경우 최소힙을 제거
            elif data[2] == "-":
                heapq.heappop(heap)
            # 공백 뒤가 아무것도 아닌 경우
            else:
                # 힙에서 가장 큰 수를 제외하고 다시 힙에 넣음
                heap = heapq.nlargest(len(heap), heap)[1:]
                heapq.heapify(heap)

    if heap:
        answer.append(max(heap))
        answer.append(min(heap))
    else:
        answer.append(0)
        answer.append(0)
    
    return answer

# solution2 : 그냥 리스트 사용

def solution(operations):
    answer = []
    result = []
    for i in operations:
        if i[0] == "I":
            answer.append(int(i[2:]))
        elif i[0] == "D":
            if len(answer) == 0:
                pass
            elif int(i[2:]) == 1:
                answer.remove(max(answer))
            else:
                answer.remove(min(answer))
                
    if answer:
        result.append(max(answer))
        result.append(min(answer))
        
    else:
        result.append(0)
        result.append(0)
    return result
    
