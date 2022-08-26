# solution 1
def solution(arr1, arr2):
    answer = [[0 for _ in range(len(arr2[0]))] for _ in range(len(arr1))]
    for i in range(len(arr1)):
        for j in range(len(arr2[0])):
            for k in range(len(arr1[0])):
                answer[i][j] += (arr1[i][k] * arr2[k][j])
    return answer
  
  # answer에 알맞은 개수 만큼 빈 리스트 설정
  # 계산을 위해 k 추가
  
  # solution 2
  def productMatrix(A, B):
    return [[sum(a*b for a, b in zip(A_row,B_col)) for B_col in zip(*B)] for A_row in A]
  
  # zip(*)
  # zip을 사용해 병렬 처리도 하고 zip(*)로 행과 열을 바꿔준다.
