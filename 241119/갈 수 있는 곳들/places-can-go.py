# n * n 격자
# 0은 이동 가능
# 1은 이동 불가
# k개의 시작점으로부터 상하좌우  이동 -> 도달 가능한 칸의 수
from collections import deque

n, k = map(int, input().split())

graph = [
    list(map(int, input().split()))
    for _ in range(n)
]

points = [
    list(map(int, input().split()))
    for _ in range(k)
]
visited = [
    [False] * n for _ in range(n)
]
dxs, dys = [1, 0, -1, 0], [0, 1, 0, -1]

def in_range(x, y):
    return 0<=x<n and 0<=y<n

def can_go(x, y):
    if not in_range(x, y):
        return False
    if graph[x][y] == 1 or visited[x][y]:
        return False
    return True 
    
for x, y in points:
    x -= 1
    y -= 1
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs, dys):
            new_x, new_y = x + dx, y + dy

            if can_go(new_x, new_y):
                visited[new_x][new_y] = True
                q.append((new_x, new_y))
                
answer = 0
for line in visited:
    answer += sum(line)        
print(answer)
        