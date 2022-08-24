from collections import deque

def bfs(p):
    start = []
    
    for i in range(5): # 시작점이 되는 P 좌표 구하기
        for j in range(5):
            if p[i][j] == 'P':
                start.append([i, j])
    
    for s in start:
        queue = deque([s])  # 큐에 초기값
        visited = [[0]*5 for i in range(5)]   # 방문 처리 리스트
        distance = [[0]*5 for i in range(5)]  # 경로 길이 리스트
        visited[s[0]][s[1]] = 1
        
        while queue:
            y, x = queue.popleft()
        
            dx = [-1, 1, 0, 0]  # 좌우
            dy = [0, 0, -1, 1]  # 상하

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0<=nx<5 and 0<=ny<5 and visited[ny][nx] == 0:              
                    if p[ny][nx] == 'O':
                        queue.append([ny, nx])
                        visited[ny][nx] = 1
                        distance[ny][nx] = distance[y][x] + 1
                    
                    if p[ny][nx] == 'P' and distance[y][x] <= 1:
                        return 0
    return 1

def solution(places):
    answer = []
    for i in places:
        answer.append(bfs(i))
    return answer
  
  # BFS를 이용해 푸는 문제. visited, distance를 만들어주고
  # 탐색하면서 X를 만나면 pass, O를 만나면 계속 탐색, P를 만나면 멈추고 거리 측정
  # 맨해튼 거리는 사실 p와 p사이에 거리였다(직관적 거리말고 요소들 통해서 갈 수 있는 거리)
