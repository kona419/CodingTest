# my answer -> not correct

def solution(participant, completion):
    answer = ''
    
    for part in participant:
        if part in completion:
            continue
        else:
            answer += part
            
    return answer
  
#answer1
def solution(participant, completion):
  participant.sort()
  completion.sort()

  for i in range(len(completion)):
      if participant[i] != completion[i]:
          return participant[i]
            
  return participant[-1]

#answer2
import collections

def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]
  
#answer3
def solution(participant, completion):
    answer = ''
    temp = 0
    dic = {}
    for part in participant:
        dic[hash(part)] = part
        temp += int(hash(part))
    for com in completion:
        temp -= hash(com)
    answer = dic[temp]

    return answer
