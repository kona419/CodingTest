# 첫번째 답 - 테스트 케이스 통과, 히든 케이스 실패
def solution(board, moves):
    answer = 0
    basket = []
    
    for m in range(len(moves)):
        for i in range(len(board)):
            if board[i][moves[m]-1] == 0:
                continue
            else:
                basket.append(board[i][moves[m]-1])
                board[i][moves[m]-1] = 0
                if len(basket) > 1 and basket[-1] == basket[-2]:
                    basket.remove(basket[-1])            # 이 부분을 basket.pop(-1) 로 바꿔주면 성공한다.
                    basket.remove(basket[-1])
                    answer+=1
                break
        
    return answer*2

  # remove 쓸 때는 안되고 pop을 쓸때는 된다.... 왜지?? 마지막 삭제는 웬만하면 pop을 쓰는 걸로..!
