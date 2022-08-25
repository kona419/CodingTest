# 내가 처음 생각한것. 딕셔너리 2개 쓰기. 근데 딕셔너리는 중복 키가 안된다. 

def solution(id_list, report, k):
    answer = []
    dic = {} #신고 횟수
    dic2 = {} #신고한애 : 신고 당한애
    for i in id_list:
        dic = {i: set()}
        dic2 = {i: set()}
    for i in id_list:
        dic[i] = 0
        
    for re in report:
        a,b = re.split()
        dic[a].add(b)
        
    for re in set(report):
        a,b = re.split()
        dic[b] += 1
    
    return dic2
  
  # 정답
  def solution(id_list, report, k):
    answer = [0] * len(id_list)    
    reports = {x : 0 for x in id_list}  #신고 당한 횟수

    for r in set(report):
        reports[r.split()[1]] += 1

    for r in set(report):
        if reports[r.split()[1]] >= k:
            answer[id_list.index(r.split()[0])] += 1  # id_list에서 신고한 사람이 있는 곳의 인덱스의 answer에 += 1

    return answer
