def solution(nums):
    
    pick = len(nums)//2
    nums = list(set(nums))
    
    if len(nums)>= pick:
        return pick
    else:
        return len(nums)
