# answer1
def solution(triangle):
    n = len(triangle)
    ans = [[0]*n for _ in range(n)]
    ans[0][0] = triangle[0][0]
    
    for x in range(1,n):
        for y in range(len(triangle[x])):
            if y==0:
                ans[x][y] = ans[x-1][0] + triangle[x][y]
            elif y == x:
                ans[x][y] = ans[x-1][y-1] + triangle[x][y]
            else:
                ans[x][y] = max(ans[x-1][y-1]+triangle[x][y], ans[x-1][y]+triangle[x][y])
            
    return max(ans[-1])
  
#answer 2
def solution(triangle):

    height = len(triangle)

    while height > 1:
        for i in range(height - 1):
            triangle[height-2][i] += max([triangle[height-1][i], triangle[height-1][i+1]])
        height -= 1

    answer = triangle[0][0]
    return answer
