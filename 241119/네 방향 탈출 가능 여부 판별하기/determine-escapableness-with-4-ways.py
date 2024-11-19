from collections import deque
n, m = map(int, input().split())

graph = [
    list(map(int, input().split()))
    for _ in range(n)
]
visited = [
    [False] * m for _ in range(n)
]
def in_range(x, y):
    return 0<=x<n and 0<=y<m

def can_go(x, y):
    if not in_range(x, y):
        return False
    
    if visited[new_x][new_y] or graph[new_x][new_y] == 0:
        return False
    
    return True 
    
    
    
q = deque([(0, 0)])

dxs, dys = [1, 0, -1, 0], [0, 1, 0, -1]
while q:
    x, y = q.popleft()
    for dx, dy in zip(dxs, dys):
        new_x, new_y = x + dx, y + dy
        if can_go(new_x, new_y):
            visited[new_x][new_y] = True
            q.append([new_x, new_y])

print(int(visited[n-1][m-1]))