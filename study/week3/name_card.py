def solution(sizes):
    max_row = 0
    max_col = 0
    
    for size in sizes:
        if size[0] < size[1]:
            size[0], size[1] = size[1], size[0]
            
    for size in sizes:
        if max_row < size[0]:
            max_row = size[0]
        if max_col < size[1]:
            max_col = size[1]
        
    return max_row*max_col
