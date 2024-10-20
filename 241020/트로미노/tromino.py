n, m = map(int, input().split())

# 17:55

grid = [
    list(map(int, input().split()))
    for _ in range(n)
] # N * M 크기의 행열

def in_range(x, y):
    return 0<=x<n and 0<=y<m

def get_max_number_in_grid(x, y):
    
    candidates = []
    if in_range(x+1, y+1):
        # .
        # ..
        candidates.append(grid[x][y] + grid[x+1][y] + grid[x+1][y+1])
        # ..
        #  .
        candidates.append(grid[x][y] + grid[x][y+1] + grid[x+1][y+1])
        #  .
        # ..
        candidates.append(grid[x][y+1] + grid[x+1][y] + grid[x+1][y+1])


    if in_range(x, y+1) and in_range(x+1, y):
        # ..
        # .
        candidates.append(grid[x][y] + grid[x][y+1] + grid[x+1][y])
    
    if in_range(x, y+2):
        # ...
        candidates.append(grid[x][y] + grid[x][y+1] + grid[x][y+2])
    
    if in_range(x+2, y):
        # .
        # .
        # .
        candidates.append(grid[x][y] + grid[x+1][y] + grid[x+2][y])
    if candidates:
        return max(candidates)
    else:
        return 0

max_number = -1
for i in range(n):
    for j in range(m):
        max_number = max(max_number, get_max_number_in_grid(i, j))
print(max_number)