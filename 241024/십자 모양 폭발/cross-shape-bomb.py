# n * n 크기의 격자판
# 특정 위치 선택 -> 그 위치 중심으로 십자 모양의 폭탄이 터짐
# 십자의 크기의 위치의 숫자에 따라 
# 터진후에는 중력에따라 떨어짐
# 1은 자기자신만 터짐
# 2는 자기 + 인접 4개
# 3은 자기 + 인접 6개

n = int(input())

grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

r, c = map(int, input().split())
r, c = r-1, c-1
K = grid[r][c]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

grid[r][c] = 0
for i in range(1, K):
    for dx, dy in zip([1, -1, 0, 0], [0, 0, 1, -1]):
        new_x, new_y = r + dx * i, c + dy * i
        if in_range(new_x, new_y):
            grid[new_x][new_y] = 0

for i in range(n-1, -1, -1):
    for j in range(0, n):
        if grid[i][j] == 0:
            for k in range(1, i+1):
                if grid[i-k][j] != 0:
                    grid[i][j] = grid[i-k][j]
                    grid[i-k][j] = 0
                    break
                
for line in grid:
    for n in line:
        print(n, end=" ")
    print()