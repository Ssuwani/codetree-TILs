n, t = map(int, input().split())

grid = [
    list(map(int, input().split()))
    for _ in range(2)
]
grid[1] = grid[1][::-1]

for _ in range(t):
    # t번 반복
    grid[0], grid[1] = grid[1][:1] + grid[0][:2], grid[1][1:] + grid[0][-1:]
grid[1] = grid[1][::-1]

for line in grid:
    for num in line:
        print(num, end=" ")
    print()