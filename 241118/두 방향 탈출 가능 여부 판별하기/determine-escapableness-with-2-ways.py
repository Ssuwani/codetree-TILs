n, m = map(int, input().split())

graph = [
    list(map(int, input().split()))
    for _ in range(n)
]
visited = [
    [False for _ in range(m)]
    for _ in range(n)
]
dxs, dys = [1, 0], [0, 1]

def in_range(x, y):
    return 0<=x<n and 0<=y<m

def can_go(x, y) -> bool:
    if not in_range(x, y):
        return False

    if graph[x][y] == 0:
        return False
    
    if visited[x][y]:
        return False

    return True
def dfs(x, y):
    for dx, dy in zip(dxs, dys):
        new_x, new_y = x + dx, y + dy
        if can_go(new_x, new_y):
            visited[new_x][new_y] = True
            dfs(new_x, new_y)
    
visited[0][0] = True
   
dfs(0, 0)
print(int(visited[n - 1][m - 1]))