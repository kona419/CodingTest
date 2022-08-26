from itertools import permutations

def solution(numbers):
    answer = []
    numbers = list(numbers)   # 숫자분리
    num = []
    new_nums = []
    for i in range(1, len(numbers)+1):     # 조합 만들기
        num += list(permutations(numbers, i))
    for n in num:            # 숫자 하나로 합치기
        new = "".join(n)
        new_nums.append(int(new))
        
    for num in new_nums:      # 소수 구하기
        if num < 2:
            continue
        check = True
        for i in range(2, int(num**0.5)+1): # n의 제곱근 보다 작을 때 까지만!
            if num%i == 0:
                check = False
                break
        if check:
            answer.append(num)
    
    return len(set(answer))
